import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.lines import Line2D
from matplotlib.patches import Patch
from pathlib import Path
from matplotlib.font_manager import FontProperties

# 与 1.py 同款字体
FONT_SANS = ["Arial", "Helvetica Neue", "DejaVu Sans"]
TEXT_COLOR = "#1E293B"

# --- 配置部分 ---
SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent
DATA_FILE = SCRIPT_DIR / "final_result.xlsx"
OUTPUT_FILE = PROJECT_ROOT / "pics" / "Figure_2.png"

# 参考图配色（用于柱状图和折线）
REFERENCE_PALETTE = [
    "#2563C7", "#F0A500", "#D35400", "#C0392B", "#6BAF3A",
    "#7B52AB", "#169BB5", "#0D2847", "#E02323",
]

# 常规标记符号
MARKERS = ["o", "s", "^", "D", "v", "<", ">", "p", "x"]

# 字体设置（字号可与 1.py 的 FS_* 独立调整）
FONT_SIZE = 16
LABEL_SIZE = 21
TICK_SIZE = 17
LEGEND_SIZE = 16
BAR_YMIN = 30
BAR_YMAX = 90
BAR_XLABEL_ROTATION = 35

# 热力图：米黄 → 青蓝 → 藏青（蓝黄色系）
HEATMAP_COLORS = [
    "#FFF9E8",
    "#FEE79A",
    "#C5E4EF",
    "#6BB6D6",
    "#3A7EBB",
    "#1C3D6E",
]
HEATMAP_CMAP = LinearSegmentedColormap.from_list("cream_yellow_blue", HEATMAP_COLORS, N=256)

plt.rcParams.update({
    "font.family": "sans-serif",
    "font.sans-serif": FONT_SANS,
    "font.size": FONT_SIZE,
    "font.weight": "normal",
    "text.color": TEXT_COLOR,
    "axes.unicode_minus": False,
    "axes.edgecolor": "#333333",
    "axes.linewidth": 1.0,
    "axes.labelsize": LABEL_SIZE,
    "axes.titlesize": LABEL_SIZE,
    "xtick.labelsize": TICK_SIZE,
    "ytick.labelsize": TICK_SIZE,
    "legend.fontsize": LEGEND_SIZE,
    "legend.frameon": False,
    "figure.dpi": 300,
    "savefig.dpi": 300,
    "savefig.bbox": "tight",
    "savefig.pad_inches": 0.06,
})

selected_models = [
    "Doubao", "Doubao FS", "Deepseek-V3", "Deepseek-V3 FS",
    "Deepseek-R1", "Qwen-Max FS", "Qwen-Max CoT", "Qwen3-235B FS", "Gemini",
]

selected_dimensions = [
    "Knowledge Question Answering",
    "Language Understanding",
    "Diagnostic Reasoning",
    "Prescription Recommendation",
    "Safety Assessment",
]

dimension_labels = [
    "Knowledge \nQA",  # Answer → QA
    "Language\nUnderstanding",
    "Diagnostic\nReasoning",
    "Prescription\nRecommend.",
    "Safety\nAssessment",
]

# --- 数据加载 ---
def load_data() -> pd.DataFrame:
    df = pd.read_excel(DATA_FILE)
    df_filtered = df[df["Model"].isin(selected_models)].copy()
    df_filtered = df_filtered[["Model"] + selected_dimensions]
    df_filtered.set_index("Model", inplace=True)
    df_filtered = df_filtered.apply(pd.to_numeric, errors="coerce")
    return df_filtered.reindex(selected_models)

# --- 图例生成 ---
def bar_legend_handles() -> list[Patch]:
    return [
        Patch(
            facecolor=REFERENCE_PALETTE[i],
            edgecolor="white",
            linewidth=0.6,
            label=model,
        )
        for i, model in enumerate(selected_models)
    ]

def heatmap_legend_elements(cmap, norm):
    # 创建自定义的颜色条图例（实际上我们会用 colorbar，这里主要为了统一风格或做特殊标注）
    # 这里我们直接返回 None，使用 ax 的 colorbar 功能
    return None

def _bar_legend_kwargs() -> dict:
    return dict(
        loc="upper center",
        bbox_to_anchor=(0.5, -0.28),
        ncol=3,
        frameon=False,
        handlelength=1.6,
        handletextpad=0.5,
        columnspacing=1.2,
        borderaxespad=0.0,
        prop=FontProperties(family="sans-serif", size=LEGEND_SIZE, weight="normal"),
    )

# --- 绘图函数 ---
def plot_grouped_bar(ax, data: pd.DataFrame) -> None:
    n_models = len(data.index)
    n_dims = len(selected_dimensions)
    x = np.arange(n_dims)
    group_width = 0.88
    bar_width = group_width / n_models

    for i, model in enumerate(data.index):
        offset = (i - (n_models - 1) / 2) * bar_width
        ax.bar(
            x + offset,
            data.loc[model, selected_dimensions].values,
            width=bar_width * 0.92,
            color=REFERENCE_PALETTE[i],
            edgecolor="white",
            linewidth=0.5,
            zorder=3,
        )

    ax.set_ylabel("Score", fontsize=LABEL_SIZE, fontweight="normal", color=TEXT_COLOR)
    ax.set_xticks(x)
    ax.set_xticklabels(
        dimension_labels,
        fontweight="normal",
        fontsize=TICK_SIZE,
        color=TEXT_COLOR,
        rotation=BAR_XLABEL_ROTATION,
        ha="right",
        rotation_mode="anchor",
    )
    ax.set_ylim(BAR_YMIN, BAR_YMAX)
    ax.set_yticks(np.arange(BAR_YMIN, BAR_YMAX + 1, 10))
    ax.tick_params(axis="both", which="major", length=3, width=0.8, colors="#333333")

    # 美化边框
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_linewidth(0.8)
    ax.spines["bottom"].set_linewidth(0.8)

    # 网格
    ax.grid(axis="y", linestyle="-", linewidth=0.5, alpha=0.35, color="#BBBBBB", zorder=0)
    ax.set_axisbelow(True)

    # 图例
    ax.legend(handles=bar_legend_handles(), **_bar_legend_kwargs())

def heatmap_text_color(norm_val: float) -> str:
    """按单元格颜色亮度自动选择黑/白文字。"""
    r, g, b, _ = HEATMAP_CMAP(np.clip(norm_val, 0, 1))
    luminance = 0.2126 * r + 0.7152 * g + 0.0722 * b
    return "#FFFFFF" if luminance < 0.58 else "#1A1A1A"

def compute_heatmap_limits(matrix: np.ndarray) -> tuple[float, float]:
    vmin = float(np.nanmin(matrix))
    vmax = float(np.nanmax(matrix))
    span = max(vmax - vmin, 1.0)
    pad = span * 0.06
    y_min = max(0.0, np.floor((vmin - pad) / 5) * 5)
    y_max = min(100.0, np.ceil((vmax + pad) / 5) * 5)
    if y_max <= y_min:
        y_min, y_max = 0.0, 100.0
    return y_min, y_max

def plot_heatmap(ax, data: pd.DataFrame) -> None:
    # 行=模型，列=维度（维度在 X 轴）
    matrix = data.to_numpy(dtype=float)
    n_rows, n_cols = matrix.shape
    vmin, vmax = compute_heatmap_limits(matrix)

    im = ax.imshow(
        matrix,
        aspect="auto",
        cmap=HEATMAP_CMAP,
        vmin=vmin,
        vmax=vmax,
        origin="upper",
        interpolation="nearest",
    )

    ax.set_xticks(np.arange(n_cols))
    ax.set_yticks(np.arange(n_rows))
    ax.set_xticklabels(
        dimension_labels,
        fontweight="normal",
        fontsize=TICK_SIZE,
        color=TEXT_COLOR,
        rotation=BAR_XLABEL_ROTATION,
        ha="right",
        rotation_mode="anchor",
    )
    ax.set_yticklabels(
        list(data.index),
        fontweight="normal",
        fontsize=TICK_SIZE,
        color=TEXT_COLOR,
    )
    ax.tick_params(axis="both", which="both", length=0, pad=6)
    ax.set_xticks(np.arange(-0.5, n_cols, 1), minor=True)
    ax.set_yticks(np.arange(-0.5, n_rows, 1), minor=True)
    ax.grid(which="minor", color="#F5F5F5", linewidth=2.0)
    ax.tick_params(which="minor", bottom=False, left=False)

    for i in range(n_rows):
        for j in range(n_cols):
            value = matrix[i, j]
            if np.isnan(value):
                continue
            norm_val = (value - vmin) / max(vmax - vmin, 1e-6)
            ax.text(
                j,
                i,
                f"{value:.1f}",
                ha="center",
                va="center",
                fontsize=TICK_SIZE,
                fontweight="normal",
                color=heatmap_text_color(norm_val),
            )

    cbar = ax.figure.colorbar(im, ax=ax, fraction=0.040, pad=0.02)
    cbar.outline.set_linewidth(0.6)
    cbar.outline.set_edgecolor("#CCCCCC")
    cbar.ax.tick_params(labelsize=TICK_SIZE, colors="#333333")
    cbar.set_label(
        "Score",
        size=LABEL_SIZE,
        weight="normal",
        color=TEXT_COLOR,
    )
    for label in cbar.ax.get_yticklabels():
        label.set_fontweight("normal")
        label.set_color(TEXT_COLOR)

    ax.set_facecolor("#FAFAFA")
    for spine in ax.spines.values():
        spine.set_visible(True)
        spine.set_linewidth(0.8)
        spine.set_color("#CCCCCC")

def main() -> None:
    data = load_data()
    print("筛选后的数据：\n", data.round(2))

    # 布局调整：
    # 左图 (Bar) 宽度 0.38，右图 (Heatmap) 宽度 0.45 (因为Heatmap需要空间放Colorbar)
    # 高度保持一致 0.58，底部留白 0.30
    fig = plt.figure(figsize=(16, 7.2))

    # 左侧柱状图区域
    ax_bar = fig.add_axes([0.06, 0.25, 0.38, 0.60])

    # 右侧热力图区域 (右边距留大一点给 colorbar)
    ax_heatmap = fig.add_axes([0.56, 0.28, 0.30, 0.46])

    plot_grouped_bar(ax_bar, data)
    plot_heatmap(ax_heatmap, data)

    fig.savefig(OUTPUT_FILE, dpi=300, facecolor="white")
    plt.close(fig)
    print(f"\n图表已保存: {OUTPUT_FILE}")

    summary = data.copy()
    summary["Average"] = summary.mean(axis=1)
    print("\n按平均分排序：\n", summary[["Average"]].sort_values("Average", ascending=False).round(2))

if __name__ == "__main__":
    main()
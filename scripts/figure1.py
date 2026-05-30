from pathlib import Path

import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.ticker as ticker
from matplotlib.patches import Rectangle
from matplotlib.transforms import blended_transform_factory
import textwrap
import numpy as np

SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent
# 与 ReadMe.md / ReadMe_cn.md 中引用的路径一致
OUTPUT_FILE = PROJECT_ROOT / "pics" / "Figure_1.png"

plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': ['Arial', 'Helvetica Neue', 'DejaVu Sans'],
    'axes.facecolor': '#FAFBFC',
    'figure.facecolor': '#FFFFFF',
    'text.color': '#1E293B',
})

# 全局字体大小
FS_TITLE = 19
FS_LABEL = 16
FS_TICK = 15
FS_GROUP = 16
FS_BAR_VAL = 15
FS_PCT = 15
FS_PIE_ANNO = 16 

TEXT_COLOR = '#000000'
LEADER_COLOR = '#B0B0B0'  # 【修改点】引导线改为浅灰色
LEADER_LW = 1.2

TOTAL = 7100

# 环形图起始角度：增大=逆时针(向左)，减小=顺时针(向右)；标注槽位固定，仅扇区与引线随角度变化
PIE_STARTANGLE = 135.0 - 22.0  # 相对基线向右旋转 22°

# 标注位置（与示意图红箭头一致）：左 / 左上 / 右上 / 右 / 下
PIE_LABEL_SLOTS = [
    (-1.58,  0.32, 'right'),   # Diagnostic Reasoning（偏左下，与 Language 拉开）
    (-1.38,  1.55, 'right'),   # Language Understanding（偏左上）
    ( 0.38,  1.38, 'right'),   # Prescription Recommendation（上中偏左，右对齐）
    ( 1.18,  1.14, 'left'),    # Safety Assessment（略向左上）
    ( 0.00, -1.52, 'center'),  # Knowledge Question Answering
]

# 配色（Tableau 系五色）
C = {
    'kqa':    '#4E79A7',
    'diag':   '#E15759',
    'lang':   '#76B7B2',
    'presc':  '#B07AA1',
    'safety': '#F28E2B',
}

DIMENSIONS = [
    ('Diagnostic Reasoning',         300,  C['diag']),
    ('Language Understanding',       300,  C['lang']),
    ('Prescription Recommendation',  300,  C['presc']),
    ('Safety Assessment',            100,  C['safety']),
    ('Knowledge Question Answering', 6100, C['kqa']),
]

GROUPS = [
    (C['diag'], [
        ('TCM-Diagnosis', 200),
        ('TCM-MSDD', 100),
    ]),
    (C['lang'], [
        ('TCMeEE', 100),
        ('TCM-CHGD', 100),
        ('TCM-LitData', 100),
    ]),
    (C['presc'], [
        ('TCM-FRD', 200),
        ('TCM-PR', 100),
    ]),
    (C['safety'], [
        ('TCM-SE-B', 50),
        ('TCM-SE-A', 50),
    ]),
    (C['kqa'], [
        ('TCM-ED-B', 4800),
        ('TCM-ED-A', 1200),
        ('TCM-FT', 100),
    ]),
]

# 子图标题：(A)/(B) 与说明同一行、加粗
PANEL_TITLES = {
    'macro': '(A) Five-Dimension Distribution',
    'micro': '(B) Twelve-Dataset Breakdown',
}

# 环形图
RING_R = 1.20
RING_W = 0.48

# 维度名称固定换行（与图 B 右侧标注一致）
DIM_MULTILINE = {
    'Diagnostic Reasoning': 'Diagnostic\nReasoning',
    'Language Understanding': 'Language\nUnderstanding',
    'Prescription Recommendation': 'Prescription\nRecommendation',
    'Safety Assessment': 'Safety\nAssessment',
    'Knowledge Question Answering': 'Knowledge\nQuestion\nAnswering',
}


def _dim_display(name):
    return DIM_MULTILINE.get(name, name)


def _pie_label(name, size, pct):
    return f'{_dim_display(name)}\n{size:,} ({pct:.1f}%)'

def _draw_pie_leader(ax, x_a, y_a, x_t, y_t):
    """扇区中点 → 标注：单段径向直线，避免折线交织"""
    ax.plot(
        [x_a, x_t], [y_a, y_t],
        color=LEADER_COLOR, lw=LEADER_LW, solid_capstyle='butt', zorder=9,
    )


def annotate_pie_leaders(ax, wedges):
    r_mid = RING_R - RING_W / 2
    for idx, (wedge, (name, size, color)) in enumerate(zip(wedges, DIMENSIONS)):
        pct = size / TOTAL * 100

        ang = np.deg2rad((wedge.theta2 + wedge.theta1) / 2)
        x_a, y_a = r_mid * np.cos(ang), r_mid * np.sin(ang)
        x_t, y_t, ha = PIE_LABEL_SLOTS[idx]

        _draw_pie_leader(ax, x_a, y_a, x_t, y_t)

        if y_t > 0.85:
            va = 'bottom'
        elif y_t < -0.85:
            va = 'top'
        else:
            va = 'center'

        ax.text(
            x_t, y_t, _pie_label(name, size, pct),
            ha=ha, va=va, fontsize=FS_PIE_ANNO, fontweight='bold',
            color=color, linespacing=1.1, zorder=10,
        )

def decorate_titles(fig, ax_macro, ax_micro):
    fig.canvas.draw()
    y_top = max(ax_macro.get_position().y1, ax_micro.get_position().y1)
    for ax, title in (
        (ax_macro, PANEL_TITLES['macro']),
        (ax_micro, PANEL_TITLES['micro']),
    ):
        cx = (ax.get_position().x0 + ax.get_position().x1) / 2
        fig.text(
            cx, y_top + 0.028, title,
            ha='center', va='bottom', fontsize=FS_TITLE, fontweight='bold', color='#1E293B',
        )

# ── 画布 ────────────────────────
fig = plt.figure(figsize=(17.5, 9), dpi=120)
gs = gridspec.GridSpec(
    1, 2, figure=fig,
    width_ratios=[0.95, 1.55], 
    left=0.08, right=0.85, bottom=0.10, top=0.82,
    wspace=0.22,
)

ax_macro = fig.add_subplot(gs[0, 0])
ax_micro = fig.add_subplot(gs[0, 1])

# ══════════════════════════════════════════════════════════
# (A) 环形图
# ══════════════════════════════════════════════════════════
sizes = [d[1] for d in DIMENSIONS]
colors = [d[2] for d in DIMENSIONS]

wedges, _ = ax_macro.pie(
    sizes,
    colors=colors,
    startangle=PIE_STARTANGLE,
    counterclock=False,
    wedgeprops=dict(width=RING_W, edgecolor='white', linewidth=2.5),
    radius=RING_R,
    center=(0, 0),
)

annotate_pie_leaders(ax_macro, wedges)

# 拓展坐标轴限制，防止放大的环形图和外推的标注被裁切
ax_macro.set_xlim(-1.88, 1.88)
ax_macro.set_ylim(-1.68, 1.72)
ax_macro.set_aspect('equal')
ax_macro.axis('off')

# ══════════════════════════════════════════════════════════
# (B) 横向条形图 + 维度标注
# ══════════════════════════════════════════════════════════
BAR_H = 0.46
INTRA_STEP = 0.54   # 组内相邻条形间距
INTER_GAP = 0.26    # 维度组之间额外留白

y_positions, y_labels, group_bounds = [], [], []
current_y = 0

for gi, (gcolor, items) in enumerate(GROUPS):
    dim_name = DIMENSIONS[gi][0]
    items_sorted = sorted(items, key=lambda x: x[1], reverse=True)
    group_start = current_y

    for name, value in items_sorted:
        ax_micro.barh(
            current_y, value, height=BAR_H, color=gcolor,
            edgecolor='white', linewidth=1.2, alpha=1.0, zorder=3,
        )
        tx = value * 1.15 if value >= 80 else value * 1.35
        ax_micro.text(
            tx, current_y, f'{value:,}',
            # 【修改点】移除了 fontweight='bold'，不加粗数量
            va='center', ha='left', fontsize=FS_BAR_VAL,
            color=TEXT_COLOR, zorder=4,
        )
        y_positions.append(current_y)
        y_labels.append(name)
        current_y -= INTRA_STEP

    group_bounds.append((group_start, y_positions[-1], dim_name, gcolor))

    if gi < len(GROUPS) - 1:
        current_y -= INTER_GAP

for y0, y1, _, _ in group_bounds[:-1]:
    y_line = (y0 + y1) / 2 - INTRA_STEP * 0.5 - INTER_GAP / 2
    ax_micro.axhline(y_line, color='#CBD5E1', linewidth=0.85, linestyle='--', zorder=1, alpha=0.8)

y_margin = 0.38
ylim = (min(y_positions) - y_margin, max(y_positions) + y_margin)
ax_micro.set_ylim(*ylim)
ax_micro.invert_yaxis()

# 维度标注
dim_xform = blended_transform_factory(ax_micro.transAxes, ax_micro.transData)
x_bar = 1.02 

def _wrap_dim_label(text):
    return _dim_display(text)

for gi, (y0, y1, dim_name, gcolor) in enumerate(group_bounds):
    y_mid = (y0 + y1) / 2
    band_h = (y1 - y0) + BAR_H * 0.4
    
    ax_micro.add_patch(Rectangle(
        (x_bar, y_mid - band_h / 2), 0.015, band_h,
        transform=dim_xform, facecolor=gcolor, edgecolor='white',
        linewidth=0.8, alpha=1.0, clip_on=False, zorder=5,
    ))
    ax_micro.text(
        x_bar + 0.025, y_mid, _wrap_dim_label(dim_name),
        transform=dim_xform, ha='left', va='center',
        fontsize=FS_GROUP, fontweight='bold', color=gcolor,
        linespacing=1.2, 
        clip_on=False, zorder=6,
    )

ax_micro.set_yticks(y_positions)
# 【修改点】移除了 fontweight='bold'，不加粗数据集名称
ax_micro.set_yticklabels(y_labels, fontsize=FS_TICK, color=TEXT_COLOR)
ax_micro.tick_params(axis='x', labelsize=FS_TICK)
ax_micro.tick_params(axis='y', length=0, pad=10)

ax_micro.set_xscale('log')
ax_micro.xaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: '{:g}'.format(x)))
max_val = max(v for _, items in GROUPS for _, v in items)
ax_micro.set_xlim(8, 10 ** (np.log10(max_val) + 0.38))

ax_micro.yaxis.grid(False)
ax_micro.xaxis.grid(True, linestyle='-', color='#E2E8F0', linewidth=0.75, zorder=0)
ax_micro.set_axisbelow(True)

for spine in ['top', 'right']:
    ax_micro.spines[spine].set_visible(False)
ax_micro.spines['left'].set_color('#CBD5E1')
ax_micro.spines['bottom'].set_color('#CBD5E1')

ax_micro.set_xlabel(
    'Number of Evaluation Items (log scale)',
    fontweight='bold', labelpad=12, fontsize=FS_LABEL, color=TEXT_COLOR,
)
ax_micro.tick_params(axis='x', colors=TEXT_COLOR)

decorate_titles(fig, ax_macro, ax_micro)

plt.savefig(OUTPUT_FILE, bbox_inches='tight', facecolor='white', dpi=150, pad_inches=0.25)
print(f"Saved: {OUTPUT_FILE}")
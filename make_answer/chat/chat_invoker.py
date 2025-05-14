class ChatInvoker:
    def chat(self, msg: str, *args, **kwargs) -> str:
        raise NotImplementedError("Subclasses must implement this method")
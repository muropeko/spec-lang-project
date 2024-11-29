class BaseConfig:
    def __init__(self, fonts=None, colors=None, justify=None):
        self.fonts = fonts if fonts is not None else []
        self.colors = colors or {
            'reset': "\033[0m",
        }
        self.justify = justify or ['left', 'center', 'right']
        self.file_path = None

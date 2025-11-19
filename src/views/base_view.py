class BaseView:
    def __init__(self, frame):
        self.frame = frame

    def mostrar(self):
        self.frame.pack(fill="both", expand=True)

    def ocultar(self):
        self.frame.pack_forget()

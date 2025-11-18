import tkinter as tk
from src.controllers.navigation import Navigation


class PantallaSeleccion:
    def __init__(self, container):
        self.nav = Navigation()
        self.frame = tk.Frame(container)

        tk.Label(self.frame, text="Selecciona o trámite", font=("Arial", 16)).pack(pady=40)

        buttons = tk.Frame(self.frame)
        buttons.pack(pady=20)

        tk.Button(buttons, text="CXT", font=("Arial", 20),
                  width=10, height=3, command=lambda: self.nav.mostrar("cxt")).pack(side="left", padx=20)

        tk.Button(buttons, text="CADP", font=("Arial", 20),
                  width=10, height=3, command=lambda: self.nav.mostrar("cadp")).pack(side="right", padx=20)

    def mostrar(self):
        self.frame.pack(fill="both", expand=True)

    def ocultar(self):
        self.frame.pack_forget()

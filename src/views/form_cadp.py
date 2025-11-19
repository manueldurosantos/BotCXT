import tkinter as tk
from src.controllers.navigation import Navigation
from src.controllers.cadp_controller import CADPController
from src.views.base_view import BaseView


class FormularioCADP(BaseView):
    def __init__(self, container):
        super().__init__(tk.Frame(container))
        self.nav = Navigation()
        self.controller = CADPController()

        self.crear_ui()

    def crear_ui(self):
        # Botón volver
        tk.Button(self.frame, text="⬅ Volver", command=lambda: self.nav.mostrar("seleccion")).pack(anchor="w", pady=8, padx=8)

        tk.Label(self.frame, text="Concurso de Adxudicación de Destinos Provisionais (CADP)", font=("Arial", 11, "bold")).pack(pady=10)
        tk.Button(self.frame, text="Abrir navegador",
                  command=lambda: self.controller.abrir_navegador("https://www.edu.xunta.gal/cadp")).pack(pady=5)

        # Ficheiro de centros
        tk.Label(self.frame, text="Ficheiro de centros:").pack()
        tk.Entry(self.frame, textvariable=self.controller.txt_archivo, width=55).pack()
        tk.Button(self.frame, text="Seleccionar ficheiro", command=self.controller.seleccionar_archivo).pack()

        # Corpo
        tk.Label(self.frame, text="Corpo:").pack()
        tk.Entry(self.frame, textvariable=self.controller.combo_corpo, width=55).pack()

        # Especialidade
        tk.Label(self.frame, text="Especialidade:").pack()
        tk.Entry(self.frame, textvariable=self.controller.combo_espec, width=55).pack()

        # Linguas
        tk.Label(self.frame, text="Linguas (separadas por punto e coma):").pack()
        tk.Entry(self.frame, textvariable=self.controller.entry_linguas, width=55).pack()

        # Afín
        tk.Checkbutton(self.frame, text="Afín", variable=self.controller.afin_checkbox).pack(pady=5)

        # Itinerancia
        tk.Label(self.frame, text="Itinerancia (indicar \"Non\" e/ou \"Si\", separadas por punto e coma):").pack()
        tk.Entry(self.frame, textvariable=self.controller.entry_itinerancia, width=55).pack()

        # Limite de destinos
        tk.Label(self.frame, text="N destinos con opcións completas (0 = todos):").pack()
        tk.Entry(self.frame, textvariable=self.controller.entry_limite, width=55).pack()

        # Lanzar proceso
        tk.Button(self.frame, text="Iniciar proceso", command=self.controller.executar).pack(pady=15)

from .base import FormularioBase
import tkinter as tk
from tkinter import messagebox
from scraper import lanzar_cadp


class FormularioCADP(FormularioBase):
    def crear_ui(self):
        self.boton_volver()
        tk.Label(self.frame, text="Concurso de Adxudicación de Destinos Provisionais (CADP)",
                 font=("Arial", 11, "bold")).pack(pady=10)
        tk.Button(self.frame, text="Abrir navegador",
                  command=lambda: self.abrir_navegador("https://www.edu.xunta.gal/cadp")).pack(pady=5)

        tk.Label(self.frame, text="Ficheiro de centros:").pack()
        tk.Entry(self.frame, textvariable=self.txt_archivo, width=55).pack()
        tk.Button(self.frame, text="Seleccionar ficheiro", command=self.seleccionar_archivo).pack()

        self.combo_corpo = tk.StringVar(value="590 - Profesores de ensino secundario")
        tk.Label(self.frame, text="Corpo:").pack()
        tk.Entry(self.frame, textvariable=self.combo_corpo, width=55).pack()

        self.combo_espec.set("590007 - Física e química")
        tk.Label(self.frame, text="Especialidade:").pack()
        tk.Entry(self.frame, textvariable=self.combo_espec, width=55).pack()

        self.afin_checkbox = tk.BooleanVar(value=False)
        tk.Checkbutton(self.frame, text="Afín", variable=self.afin_checkbox).pack(pady=5)

        self.entry_linguas.set("Non bilingüe;Inglés")
        tk.Label(self.frame, text="Linguas (separadas por punto e coma):").pack()
        tk.Entry(self.frame, textvariable=self.entry_linguas, width=55).pack()

        self.entry_itinerancia.set("Non")
        tk.Label(self.frame, text="Itinerancia (separadas por punto e coma):").pack()
        tk.Entry(self.frame, textvariable=self.entry_itinerancia, width=55).pack()

        tk.Label(self.frame, text="N destinos con opcións completas (0 = todos):").pack()
        tk.Entry(self.frame, textvariable=self.entry_limite, width=55).pack()

        tk.Button(self.frame, text="Iniciar proceso", command=self.executar).pack(pady=15)

    def executar(self):
        try:
            valores = self.obter_valores_comuns()
            driver = self.abrir_navegador("https://www.edu.xunta.gal/cadp")
            lanzar_cadp(driver,
                        centros=open(valores["txt_archivo"]).read().split(),
                        corpo=self.combo_corpo.get(),
                        especialidade=valores["especialidade"],
                        linguas=valores["linguas"],
                        afin=self.afin_checkbox.get(),
                        itinerancias=valores["itinerancias"],
                        limite=valores["limite"])
            messagebox.showinfo("Proceso finalizado", "Completado con éxito")
        except Exception as e:
            messagebox.showerror("Erro", f"Houbo un erro no proceso: \n{e}")

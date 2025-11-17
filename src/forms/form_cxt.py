from .base import FormularioBase
import tkinter as tk
from tkinter import messagebox
from scraper import lanzar_cxt

class FormularioCXT(FormularioBase):
    def crear_ui(self):
        self.boton_volver()
        tk.Label(self.frame, text="Concurso Xeral de Traslados (CXT)", font=("Arial", 11, "bold")).pack(pady=10)
        tk.Button(self.frame, text="Abrir navegador",
                  command=lambda: self.abrir_navegador("https://www.edu.xunta.gal/cxt")).pack(pady=5)

        tk.Label(self.frame, text="Ficheiro de centros:").pack()
        tk.Entry(self.frame, textvariable=self.txt_archivo, width=55).pack()
        tk.Button(self.frame, text="Seleccionar ficheiro", command=self.seleccionar_archivo).pack()

        self.combo_ente = tk.StringVar(value="11-Galicia")
        tk.Label(self.frame, text="Ente do vernáculo:").pack()
        tk.Entry(self.frame, textvariable=self.combo_ente, width=55).pack()

        self.combo_vernaculo = tk.StringVar(value="0-SEN REQUISITO LINGÜISTICO")
        tk.Label(self.frame, text="Vernáculo:").pack()
        tk.Entry(self.frame, textvariable=self.combo_vernaculo, width=55).pack()

        self.combo_espec.set("590007-FÍSICA E QUÍMICA")
        tk.Label(self.frame, text="Especialidade:").pack()
        tk.Entry(self.frame, textvariable=self.combo_espec, width=55).pack()

        tk.Label(self.frame, text="Linguas (separadas por punto e coma):").pack()
        tk.Entry(self.frame, textvariable=self.entry_linguas, width=55).pack()

        tk.Label(self.frame, text="Itinerancia (separadas por punto e coma):").pack()
        tk.Entry(self.frame, textvariable=self.entry_itinerancia, width=55).pack()

        tk.Label(self.frame, text="N destinos con opcións completas (0 = todos):").pack()
        tk.Entry(self.frame, textvariable=self.entry_limite, width=55).pack()

        tk.Button(self.frame, text="Iniciar proceso", command=self.executar).pack(pady=15)

    def executar(self):
        try:
            valores = self.obter_valores_comuns()
            driver = self.abrir_navegador("https://www.edu.xunta.gal/cxt")
            lanzar_cxt(driver,
                       centros=open(valores["txt_archivo"]).read().split(),
                       especialidade=valores["especialidade"],
                       ente=self.combo_ente.get(),
                       vernaculo=self.combo_vernaculo.get(),
                       linguas=valores["linguas"],
                       itinerancias=valores["itinerancias"],
                       limite=valores["limite"])
            messagebox.showinfo("Proceso finalizado", "Completado con éxito")
        except Exception as e:
            messagebox.showerror("Erro", f"Houbo un erro no proceso: \n{e}")

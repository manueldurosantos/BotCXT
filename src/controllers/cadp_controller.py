import tkinter as tk
from src.controllers.base_controller import BaseController
from src.models.scraper import lanzar_cadp
from tkinter import messagebox


class CADPController(BaseController):
    def __init__(self):
        super().__init__()
        self.combo_corpo = tk.StringVar(value="590 - Profesores de ensino secundario")
        self.combo_espec = tk.StringVar(value="590007 - Física e química")
        self.afin_checkbox = tk.BooleanVar(value=False)
        self.entry_linguas = tk.StringVar(value="Non bilingüe;Inglés")
        self.entry_itinerancia = tk.StringVar(value="Non")

    def executar(self):
        driver = self.get_driver()
        try:
            centros = open(self.txt_archivo.get()).read().split()
            lanzar_cadp(
                driver=driver,
                centros=centros,
                corpo=self.combo_corpo.get(),
                especialidade=self.combo_espec.get(),
                linguas=[l.strip() for l in self.entry_linguas.get().split(";")],
                afin=self.afin_checkbox.get(),
                itinerancias=[i.strip() for i in self.entry_itinerancia.get().split(";")],
                limite=int(self.entry_limite.get())
            )
            messagebox.showinfo("Proceso finalizado", "Completado con éxito")
        except Exception as e:
            messagebox.showerror("❌ Erro", f"Houbo un erro no proceso: \n{e}")

import tkinter as tk
from src.controllers.base_controller import BaseController
from src.models.scraper import lanzar_cxt
from tkinter import messagebox


class CXTController(BaseController):
    def __init__(self):
        super().__init__()
        self.combo_espec = tk.StringVar(value="590007-FÍSICA E QUÍMICA")
        self.combo_ente = tk.StringVar(value="11-Galicia")
        self.combo_vernaculo = tk.StringVar(value="0-SEN REQUISITO LINGÜISTICO")
        self.entry_linguas = tk.StringVar(value="-- Sen indicar --;2-INGLÉS")
        self.entry_itinerancia = tk.StringVar(value="0-Non")

    def executar(self):
        driver = self.get_driver()
        try:
            centros = open(self.txt_archivo.get()).read().split()
            lanzar_cxt(
                driver=driver,
                centros=centros,
                especialidade=self.combo_espec.get(),
                ente=self.combo_ente.get(),
                vernaculo=self.combo_vernaculo.get(),
                linguas=[l.strip() for l in self.entry_linguas.get().split(";")],
                itinerancias=[i.strip() for i in self.entry_itinerancia.get().split(";")],
                limite=int(self.entry_limite.get())
            )
            messagebox.showinfo("Proceso finalizado", "Completado con éxito")
        except Exception as e:
            messagebox.showerror("❌ Erro", f"Houbo un erro no proceso: \n{e}")

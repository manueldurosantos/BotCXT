import tkinter as tk
from tkinter import messagebox
import time
from src.controllers.base_controller import BaseController
from src.models.scraper import lanzar_cxt
from src.models.logger import Logger


class CXTController(BaseController):
    def __init__(self):
        super().__init__()
        self.combo_espec = tk.StringVar(value="590007-FÍSICA E QUÍMICA")
        self.combo_ente = tk.StringVar(value="11-Galicia")
        self.combo_vernaculo = tk.StringVar(value="0-SEN REQUISITO LINGÜISTICO")
        self.entry_linguas = tk.StringVar(value="-- Sen indicar --;2-INGLÉS")
        self.entry_itinerancia = tk.StringVar(value="0-Non")

    def executar(self):
        start_time = time.time()
        driver = self.get_driver()
        centros = []
        status = ""
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
            status = "Exitoso"
        except Exception as e:
            status = f"Erro: {e}"
        finally:
            Logger.inserir_log_async(
                tramite="CXT",
                centros=len(centros),
                especialidade=self.combo_espec.get(),
                linguas=self.entry_linguas.get(),
                itinerancias=self.entry_itinerancia.get(),
                status=status,
                duracion=round(time.time() - start_time, 2)
            )
            if status == "Exitoso":
                messagebox.showinfo("Proceso finalizado", "Completado con éxito")
            else:
                messagebox.showerror("❌ Erro", f"{status}")

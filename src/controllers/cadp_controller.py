import tkinter as tk
from tkinter import messagebox
import time
from src.controllers.base_controller import BaseController
from src.models.scraper import lanzar_cadp
from src.models.logger import Logger


class CADPController(BaseController):
    def __init__(self):
        super().__init__()
        self.combo_corpo = tk.StringVar(value="590 - Profesores de ensino secundario")
        self.combo_espec = tk.StringVar(value="590007 - Física e química")
        self.afin_checkbox = tk.BooleanVar(value=False)
        self.entry_linguas = tk.StringVar(value="Non bilingüe;Inglés")
        self.entry_itinerancia = tk.StringVar(value="Non")

    def executar(self):
        start_time = time.time()
        centros = []
        status = ""
        try:
            centros = open(self.txt_archivo.get()).read().split()
            lanzar_cadp(
                driver=BaseController.driver,
                centros=centros,
                corpo=self.combo_corpo.get(),
                especialidade=self.combo_espec.get(),
                linguas=[l.strip() for l in self.entry_linguas.get().split(";")],
                afin=self.afin_checkbox.get(),
                itinerancias=[i.strip() for i in self.entry_itinerancia.get().split(";")],
                limite=int(self.entry_limite.get())
            )
            status = "Exitoso"
        except Exception as e:
            status = f"Erro: {e}"
        finally:
            Logger.inserir_log_async(
                tramite="CADP",
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
                messagebox.showerror("❌ Erro", f"Asegúrate de que tes aberta a pestana \"Peticións\" antes de executar.\n\n{status}")

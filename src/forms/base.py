import tkinter as tk
from tkinter import filedialog
from selenium.common import WebDriverException
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver

driver = None  # webdriver compartido

class FormularioBase:
    def __init__(self, container, volver_a_seleccion):
        self.container = container
        self.volver_a_seleccion = volver_a_seleccion
        self.frame = tk.Frame(container)
        self.txt_archivo = tk.StringVar()
        self.combo_espec = tk.StringVar()
        self.entry_linguas = tk.StringVar(value="-- Sen indicar --;2-INGLÉS")
        self.entry_itinerancia = tk.StringVar(value="0-Non")
        self.entry_limite = tk.StringVar(value="0")

    def boton_volver(self):
        tk.Button(self.frame, text="⬅ Volver", command=self.volver).pack(anchor="w", pady=8, padx=8)

    def volver(self):
        self.frame.pack_forget()
        self.volver_a_seleccion()

    def seleccionar_archivo(self):
        ruta = filedialog.askopenfilename()
        self.txt_archivo.set(ruta)

    def abrir_navegador(self, url):
        global driver
        driver_started = False
        if driver is not None:
            try:
                if driver.window_handles:
                    driver_started = True
            except WebDriverException:
                driver_started = False

        if not driver_started:
            driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
            driver.get(url)
        return driver

    def obter_valores_comuns(self):
        return {
            "txt_archivo": self.txt_archivo.get(),
            "especialidade": self.combo_espec.get(),
            "linguas": [l.strip() for l in self.entry_linguas.get().split(";")],
            "itinerancias": [i.strip() for i in self.entry_itinerancia.get().split(";")],
            "limite": int(self.entry_limite.get())
        }

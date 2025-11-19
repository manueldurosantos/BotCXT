import tkinter as tk
from tkinter import filedialog
from selenium.common import WebDriverException
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver


class BaseController:
    driver = None
    def __init__(self):
        self.txt_archivo = tk.StringVar()
        self.entry_limite = tk.StringVar(value="0")

    def seleccionar_archivo(self):
        ruta = filedialog.askopenfilename()
        self.txt_archivo.set(ruta)

    @staticmethod
    def abrir_navegador(url):
        driver_started = False
        if BaseController.driver is not None:
            try:
                if BaseController.driver.window_handles:
                    driver_started = True
            except WebDriverException:
                driver_started = False

        if not driver_started:
            BaseController.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
            BaseController.driver.get(url)
        return BaseController.driver

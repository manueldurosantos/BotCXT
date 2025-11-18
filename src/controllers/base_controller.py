import tkinter as tk
from tkinter import filedialog
from selenium.common import WebDriverException
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver

driver = None  # webdriver compartido


class BaseController:
    def __init__(self):
        self.txt_archivo = tk.StringVar()
        self.entry_limite = tk.StringVar(value="0")

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

    def get_driver(self):
        global driver
        return driver

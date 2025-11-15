import tkinter as tk
from tkinter import filedialog, messagebox
from selenium import webdriver
from selenium.common import WebDriverException
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from scraper import lanzar

driver = None
def seleccionar_archivo():
    ruta = filedialog.askopenfilename()
    txt_archivo.set(ruta)

def abrir():
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
        driver.get("https://www.edu.xunta.gal/cxt")

def executar():
    global driver
    try:
        centros = open(txt_archivo.get()).read().split()
        ente = combo_ente.get()
        vernaculo = combo_vernaculo.get()
        especialidade = combo_espec.get()
        linguas = [lingua.strip() for lingua in entry_linguas.get().split(";")]
        itinerancias = [itinerancia.strip() for itinerancia in entry_itinerancia.get().split(";")]
        limite = int(entry_limite.get())

        lanzar(driver, centros, especialidade, ente, vernaculo, linguas, itinerancias, limite)
        messagebox.showinfo("Proceso finalizado", "Completado con éxito")
    except Exception as e:
        messagebox.showerror("Erro", f"Houbo un erro no proceso: \n{e}")


if __name__ == "__main__":
    root = tk.Tk()
    root.title("BotCXT")
    root.geometry("450x400")

    txt_archivo = tk.StringVar()

    tk.Button(root, text="Abrir navegador", command=abrir).pack(pady=15)

    tk.Label(root, text="Ficheiro de centros:").pack()
    tk.Entry(root, textvariable=txt_archivo, width=50).pack()
    tk.Button(root, text="Seleccionar ficheiro", command=seleccionar_archivo).pack()

    combo_espec = tk.StringVar(value="590007-FÍSICA E QUÍMICA")
    tk.Label(root, text="Especialidade:").pack()
    tk.Entry(root, textvariable=combo_espec, width=50).pack()

    combo_ente = tk.StringVar(value="11-Galicia")
    tk.Label(root, text="Ente do vernáculo:").pack()
    tk.Entry(root, textvariable=combo_ente, width=50).pack()

    combo_vernaculo = tk.StringVar(value="0-SEN REQUISITO LINGÜISTICO")
    tk.Label(root, text="Vernáculo:").pack()
    tk.Entry(root, textvariable=combo_vernaculo, width=50).pack()

    entry_linguas = tk.StringVar(value="-- Sen indicar --;2-INGLÉS")
    tk.Label(root, text="Linguas (separadas por punto e coma):").pack()
    tk.Entry(root, textvariable=entry_linguas, width=50).pack()

    entry_itinerancia = tk.StringVar(value="0-Non")
    tk.Label(root, text="Itinerancia (separadas por punto e coma):").pack()
    tk.Entry(root, textvariable=entry_itinerancia, width=50).pack()

    entry_limite = tk.StringVar(value="0")
    tk.Label(root, text="N destinos con opcións completas (0 = todos):").pack()
    tk.Entry(root, textvariable=entry_limite, width=50).pack()

    tk.Button(root, text="Iniciar proceso", command=executar).pack(pady=5)

    root.mainloop()

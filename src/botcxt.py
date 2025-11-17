import tkinter as tk
import webbrowser
from forms.form_cxt import FormularioCXT
from forms.form_cadp import FormularioCADP

VERSION = "20251117.0"
root = tk.Tk()
root.title("Bot CXT/CADP")
root.geometry("520x520")
root.resizable(False, False)

container = tk.Frame(root)
container.pack(fill="both", expand=True)

pantallas = {}


class PantallaSeleccion:
    def __init__(self, container, mostrar_cxt, mostrar_cadp):
        self.frame = tk.Frame(container)
        tk.Label(self.frame, text="Selecciona o trámite", font=("Arial", 16)).pack(pady=40)
        frame_botons = tk.Frame(self.frame)
        frame_botons.pack(pady=20)

        tk.Button(frame_botons, text="CXT", font=("Arial", 20), width=10, height=3,
                  command=mostrar_cxt).pack(side="left", padx=20)
        tk.Button(frame_botons, text="CADP", font=("Arial", 20), width=10, height=3,
                  command=mostrar_cadp).pack(side="right", padx=20)

    def mostrar(self):
        self.frame.pack(fill="both", expand=True)

    def ocultar(self):
        self.frame.pack_forget()

def mostrar_cxt():
    pantallas["seleccion"].ocultar()
    pantallas["cxt"].frame.pack(fill="both", expand=True)

def mostrar_cadp():
    pantallas["seleccion"].ocultar()
    pantallas["cadp"].frame.pack(fill="both", expand=True)

pantallas["cxt"] = FormularioCXT(container, lambda: pantallas["seleccion"].mostrar())
pantallas["cxt"].crear_ui()
pantallas["cadp"] = FormularioCADP(container, lambda: pantallas["seleccion"].mostrar())
pantallas["cadp"].crear_ui()

pantallas["seleccion"] = PantallaSeleccion(container, mostrar_cxt, mostrar_cadp)
pantallas["seleccion"].mostrar()

# --- FOOTER ---
footer = tk.Frame(root)
footer.pack(side="bottom", fill="x", pady=5, padx=10)

label_centros = tk.Label(footer, text="Colemaps: ficheiro de centros", fg="blue", cursor="hand2", font=("Arial", 8, "underline"))
label_centros.pack(side="left")
label_centros.bind("<Button-1>", lambda e: webbrowser.open("https://profesoradogalicia.com/colemaps/"))

label_version = tk.Label(footer, text=f"v{VERSION}", font=("Arial", 8), fg="gray")
label_version.pack(side="right", padx=(0,5))
label_github = tk.Label(footer, text="GitHub", font=("Arial", 8, "underline"), fg="blue", cursor="hand2")
label_github.pack(side="right", padx=(0,5))
label_github.bind("<Button-1>", lambda e: webbrowser.open("https://github.com/manueldurosantos/BotCXT"))


root.mainloop()

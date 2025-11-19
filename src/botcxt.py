import tkinter as tk
import webbrowser
from src.controllers.navigation import Navigation
from src.views.pantalla_seleccion import PantallaSeleccion
from src.views.form_cxt import FormularioCXT
from src.views.form_cadp import FormularioCADP
from src.config.version import VERSION


root = tk.Tk()
root.title("Bot CXT/CADP")
root.geometry("520x520")
root.resizable(False, False)

container = tk.Frame(root)
container.pack(fill="both", expand=True)

nav = Navigation()

p_sel = PantallaSeleccion(container)
p_cxt = FormularioCXT(container)
p_cadp = FormularioCADP(container)

nav.rexistrar("seleccion", p_sel)
nav.rexistrar("cxt", p_cxt)
nav.rexistrar("cadp", p_cadp)
nav.mostrar("seleccion")

# FOOTER
footer = tk.Frame(root)
footer.pack(side="bottom", fill="x", pady=5, padx=10)

l_centros = tk.Label(footer, text="Colemaps: ficheiro de centros", fg="blue", cursor="hand2",
                     font=("Arial", 8, "underline"))
l_centros.pack(side="left")
l_centros.bind("<Button-1>", lambda e: webbrowser.open("https://profesoradogalicia.com/colemaps/"))

tk.Label(footer, text=f"v{VERSION}", font=("Arial", 8), fg="gray").pack(side="right", padx=5)
link = tk.Label(footer, text="GitHub", font=("Arial", 8, "underline"), fg="blue", cursor="hand2")
link.pack(side="right", padx=5)
link.bind("<Button-1>", lambda e: webbrowser.open("https://github.com/manueldurosantos/BotCXT"))

root.mainloop()

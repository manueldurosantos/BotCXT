class Navigation:
    pantallas = {}

    def rexistrar(self, nome, pantalla):
        Navigation.pantallas[nome] = pantalla

    def mostrar(self, nome):
        for p in Navigation.pantallas.values():
            p.ocultar()
        Navigation.pantallas[nome].mostrar()

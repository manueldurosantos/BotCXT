class Navigation:
    pantallas = {}

    @staticmethod
    def rexistrar(nome, pantalla):
        Navigation.pantallas[nome] = pantalla

    @staticmethod
    def mostrar(nome):
        for p in Navigation.pantallas.values():
            p.ocultar()
        Navigation.pantallas[nome].mostrar()

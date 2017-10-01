
class Estadisticas():
    def calcular(self, cadena):
        if cadena != "":
            if "," in cadena:
                return [2]
            else:
                return [1]
        else:
            return []

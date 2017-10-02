
class Estadisticas():
    def calcular(self, cadena):
        if cadena != "":
            numeros = cadena.split(",")
            return [len(numeros)]
        else:
            return []

    def minimo (self,cadena):
        if cadena != "":
            if "," in cadena:
                return [2]
            else:
                return [1]
        else:
            return[0]
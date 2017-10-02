
class Estadisticas():
    def calcular(self, cadena):
        if cadena != "":
            numeros = cadena.split(",")
            return [len(numeros)]
        else:
            return []

    def minimo (self,cadena):
        if cadena != "":
            numeros = cadena.split(",")
            return [len (numeros), min(numeros)]
        else:
            return[]

    def maximo (self,cadena):
        if cadena != "":
            numeros = cadena.split(",")
            return [len(numeros), min(numeros), max(numeros)]
        else:
            return []



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

    def promedio(self, cadena):
        if cadena != "":
            if len(cadena) > 1:
                numeros = cadena.split(",")
                promedio = (int(numeros[0])+int(numeros[1]))/2
                return [len(numeros), min(numeros), max(numeros),promedio]
            else:
                return [int(cadena)]
        else:
            return []
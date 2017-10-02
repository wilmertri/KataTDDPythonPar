
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
                total = 0
                for n in numeros:
                    sum_num = int(n)
                    total += sum_num

                promedio = total/len(numeros)
                return [len(numeros), min(numeros), max(numeros),promedio]
            else:
                return [int(cadena)]
        else:
            return []
from unittest import TestCase

from Estadisticas import Estadisticas

class EstadisticasTest(TestCase):
    def test_calcular(self):
        self.assertEqual(Estadisticas().calcular(""),[],"Cadena vacia")

    def test_calcular_conUnNumero(self):
        self.assertEqual(Estadisticas().calcular("1"),[1],"Un numero")

    def test_calcular_conDosNumeros(self):
        self.assertEqual(Estadisticas().calcular("1,3"),[2],"Dos numeros")

    def test_calcular_conMultiplesNumeros(self):
        self.assertEqual(Estadisticas().calcular("1,3,4,8"),[4],"Multiples numeros")

    def test_minimo(self):
        self.assertEqual(Estadisticas().minimo(""),[],"Cadena vacia")

    def test_minimo_conUnNumero(self):
        self.assertEqual(Estadisticas().minimo("1"), [1], "Un numero")

    def test_minimo_conDosNumeros(self):
        self.assertEqual(Estadisticas().minimo("1,3"), [2], "Dos numeros")

    def test_calcular_conMultiplesNumeros(self):
        self.assertEqual(Estadisticas().calcular("1,3,4,8"),[4],"Multiples numeros")


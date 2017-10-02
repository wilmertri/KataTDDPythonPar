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
        self.assertEqual(Estadisticas().minimo(""), [], "Cadena vacia")

    def test_minimo_conUnNumero(self):
        self.assertEqual(Estadisticas().minimo("1"), [1,'1'], "Un numero")

    def test_minimo_conDosNumeros(self):
        self.assertEqual(Estadisticas().minimo("8,3"), [2,'3'], "Dos numeros")

    def test_minimo_conMultiplesNumeros(self):
        self.assertEqual(Estadisticas().minimo("1,3,4,8"), [4,'1'], "Multiples numeros")

    def test_maximo(self):
        self.assertEqual(Estadisticas().maximo(""), [], "Cadena vacia")

    def test_maximo_conUnNumero(self):
        self.assertEqual(Estadisticas().maximo("1"), [1,'1','1'], "Un numero")

    def test_maximo_conDosNumeros(self):
        self.assertEqual(Estadisticas().maximo("8,3"), [2,'3','8'], "Dos numeros")

    def test_maximo_conMultiplesNumeros(self):
        self.assertEqual(Estadisticas().maximo("1,3,4,8"), [4,'1','8'], "Multiples numeros")

    def test_promedio(self):
        self.assertEqual(Estadisticas().promedio(""),[],"Cadena vacia")

    def test_promedio(self):
        self.assertEqual(Estadisticas().promedio("4"),[4],"Un numero")


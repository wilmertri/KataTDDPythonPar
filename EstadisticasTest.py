from unittest import TestCase

from Estadisticas import Estadisticas

class EstadisticasTest(TestCase):
    def test_calcular(self):
        self.assertEqual(Estadisticas().calcular(""),[],"Cadena vacia")

    def test_calcular_conUnNumero(self):
        self.assertEqual(Estadisticas().calcular("1"),[1],"Un numero")

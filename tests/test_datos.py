import unittest
from datos import peliculas


class TestDatos(unittest.TestCase):
    def test_peliculas(self):

        resultado = peliculas()
        self.assertEqual(len(resultado), 10)
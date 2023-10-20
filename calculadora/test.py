
from calculadora import sumar, restar, multiplicar, dividir, comprobarPar, comprobarMayores
import unittest


class TestCalculaMedia(unittest.TestCase):

    def testSumar(self):
        resultado = sumar(5, 5)
        self.assertEqual(resultado, 10)

    def testrestar(self):
        resultado = restar(5, 5)
        self.assertEqual(resultado, 0)

    def testMultiplicar(self):
        resultado = multiplicar(5, 5)
        self.assertEqual(resultado, 25)

    def testDividir(self):
        resultado = dividir(10, 2)
        self.assertEqual(resultado, 5)

    def testPar(self):
        resultado = comprobarPar(5)
        self.assertEqual(resultado, True)

    def testMayores(self):
        resultado = comprobarMayores(5, 10)
        self.assertEqual(resultado, True)


if __name__ == '__main__':
    unittest.main()
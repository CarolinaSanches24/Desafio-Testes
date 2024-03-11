# Gravar testes usando unittest

# Executar testes

import unittest

def soma(a, b):
    return a + b

class TestCalculadora(unittest.TestCase):
    def test_soma_positivos(self):
        resultado = soma(3, 5)
        self.assertEqual(resultado, 8)

    def test_soma_negativos(self):
        resultado = soma(-2, -4)
        self.assertEqual(resultado, -6)

    def test_soma_misto(self):
        resultado = soma(10, -7)
        self.assertEqual(resultado, 3)

    def test_soma_zero(self):
        resultado = soma(0, 9)
        self.assertEqual(resultado, 9)

if __name__ == '__main__':
    unittest.main()



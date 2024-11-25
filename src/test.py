import unittest
import numpy as np
from poly import GF2Polynomial  
import os
#Перепроверить тесты
class TestGF2Polynomial(unittest.TestCase):

    def setUp(self):
        # Завжди перед кожним тестом ініціалізуємо стандартний поліном
        self.poly1 = GF2Polynomial([1, 0, 1])  # x^2 + 1
        self.poly2 = GF2Polynomial([1, 1])  # x + 1
        self.poly3 = GF2Polynomial([1, 0, 1, 0])  # x^3 + x + 1

    def test_addition(self):
        # Перевіримо додавання поліномів
        result = self.poly1 + self.poly2
        expected = GF2Polynomial([1, 1, 0])  # x^2 + x + 
        self.assertEqual(result, expected)

    def test_multiplication(self):
        # Перевіримо множення поліномів
        result = self.poly1 * self.poly2
        expected = GF2Polynomial([1, 1, 1])  # x^2 + x + 1
        self.assertEqual(result, expected)

    def test_square(self):
        # Перевіримо возведення в квадрат
        result = self.poly1.square()
        expected = GF2Polynomial([1, 0, 1, 0])  # x^4 + x^2 + 1
        self.assertEqual(result, expected)

    def test_power(self):
        # Перевіримо піднесення до степеня
        result = self.poly1.power(3)
        expected = GF2Polynomial([1, 0, 1, 0])  # x^3 + x + 1 (по аналогії з методом reduce)
        self.assertEqual(result, expected)

    def test_reduce(self):
        # Перевіримо редукцію полінома
        coeffs = np.array([1, 1, 0, 0, 1, 1])  # x^5 + x^4 + x^1 + 1
        reduced_poly = self.poly1.reduce(coeffs)
        expected = GF2Polynomial([1, 1, 1])  # Після редукції має вийти x^2 + x + 1
        self.assertEqual(reduced_poly, expected)

    def test_trim(self):
        # Перевіримо, чи працює trim для усунення зайвих нулів
        poly_with_trailing_zeros = GF2Polynomial([1, 0, 0, 1, 0])  # x^4 + 1
        #need to 
                #need to rewright
        #incorrect tests
        poly_with_trailing_zeros.trim()
        expected = GF2Polynomial([1, 0, 0, 1])  # x^4 + 1
        self.assertEqual(poly_with_trailing_zeros, expected)

    def test_empty_polynomial(self):
        # Перевіримо випадок з порожнім поліномом
        empty_poly = GF2Polynomial([0])  # Порожній поліном (0)

        #changes123123124124124124
        
        
        self.assertEqual(empty_poly, GF2Polynomial([0]))

if __name__ == '__main__':
    unittest.main()

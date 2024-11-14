import numpy as np
from dotenv import load_dotenv
import os

# Завантажуємо .env файл
load_dotenv()

class GF2Polynomial:
    def __init__(self, coeffs):
        """
        Ініціалізація елемента в полі GF(2^491).
        :param coeffs: Список коефіцієнтів у вигляді [c_0, c_1, ..., c_n] зі значеннями 0 або 1.
        """
        self.coeffs = np.array(coeffs, dtype=np.int8) % 2
        self.trim()

    def trim(self):
        """Видаляє зайві старші нулі для правильного представлення."""
        self.coeffs = np.trim_zeros(self.coeffs, 'f') or np.array([0], dtype=np.int8)

    def __add__(self, other):
        """
        Операція додавання (XOR) двох елементів поля GF(2).
        :param other: інший елемент GF2Polynomial
        :return: новий GF2Polynomial після XOR
        """
        max_len       = max(len(self.coeffs), len(other.coeffs))
        padded_self   = np.pad(self.coeffs, (max_len - len(self.coeffs), 0))
        padded_other  = np.pad(other.coeffs, (max_len - len(other.coeffs), 0))
        result_coeffs = np.bitwise_xor(padded_self, padded_other)  # Використання XOR
        return GF2Polynomial(result_coeffs)
    
    def __mul__(self, poly_generator):
        #result_coeffs = np.zeros(len(self.coeffs) + len(other.coeffs) - 1, dtype=np.int8)
        pass

    def __repr__(self):
        return f"GF2Polynomial({self.coeffs.tolist()})"


# Завантажуємо значення полінома генератора з .env файлу
generator_coeffs_str = os.getenv('GENERATOR_POLYNOMIAL')
generator_coeffs = np.array(eval(os.getenv("GENERATOR_POLYNOMIAL")), dtype=np.int8)

# Ініціалізуємо поліном генератор
generator_polynomial = GF2Polynomial(generator_coeffs)

# Виводимо поліном генератор
print("Generator Polynomial:", generator_polynomial)

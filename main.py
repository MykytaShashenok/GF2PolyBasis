import numpy as np

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
        self.coeffs = np.trim_zeros(self.coeffs, 'f')
        if len(self.coeffs) == 0:
            self.coeffs = np.array([0], dtype=np.int8)  # Забезпечуємо ненульову довжину для нульового полінома

    def __add__(self, other):
        """
        Операція додавання (XOR) двох елементів поля GF(2).
        :param other: інший елемент GF2Polynomial
        :return: новий GF2Polynomial після XOR
        """
        max_len = max(len(self.coeffs), len(other.coeffs))
        padded_self = np.pad(self.coeffs, (max_len - len(self.coeffs), 0))
        padded_other = np.pad(other.coeffs, (max_len - len(other.coeffs), 0))
        result_coeffs = np.bitwise_xor(padded_self, padded_other)  # Використання XOR
        return GF2Polynomial(result_coeffs)

    def __repr__(self):
        return f"GF2Polynomial({self.coeffs.tolist()})"
    
# Два елементи в полі GF(2^491)
p1 = GF2Polynomial([1, 0, 1, 1])  # Поліном x^3 + x + 1
p2 = GF2Polynomial([1, 1, 0, 1])  # Поліном x^3 + x^2 + 1

# Додавання
p3 = p1 + p2
print("p1 + p2 =", p3)

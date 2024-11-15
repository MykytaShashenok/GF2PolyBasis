import numpy as np
from dotenv import load_dotenv
import os

load_dotenv()

class GF2Polynomial:
    def __init__(self, coeffs):
        self.coeffs = np.array(coeffs, dtype=np.int8) % 2
        self.trim()

    def trim(self):
        self.coeffs = np.trim_zeros(self.coeffs, 'f')

    def __add__(self, other):
        max_len = max(len(self.coeffs), len(other.coeffs))
        padded_self = np.pad(self.coeffs, (max_len - len(self.coeffs), 0))
        padded_other = np.pad(other.coeffs, (max_len - len(other.coeffs), 0))
        result_coeffs = np.bitwise_xor(padded_self, padded_other)
        return GF2Polynomial(result_coeffs)
    
    def __mul__(self, other):
        result_coeffs = np.zeros(len(self.coeffs) + len(other.coeffs) - 1, dtype=np.int8)
        for i in range(len(self.coeffs)):
            result_coeffs[i:i + len(other.coeffs)] ^= self.coeffs[i] * other.coeffs
        
        while len(result_coeffs) >= len(generator_polynomial.coeffs):
            if result_coeffs[0] == 1:
                result_coeffs[:len(generator_polynomial.coeffs)] ^= generator_polynomial.coeffs
            result_coeffs = np.trim_zeros(result_coeffs, 'f') or np.array([0], dtype=np.int8)
        
        return GF2Polynomial(result_coeffs)

    def __repr__(self):
        return f"GF2Polynomial({self.coeffs.tolist()})"


generator_coeffs_str = os.getenv('GENERATOR_POLYNOMIAL')
generator_coeffs     = np.array(eval(os.getenv("GENERATOR_POLYNOMIAL")), dtype=np.int8)
generator_polynomial = GF2Polynomial(generator_coeffs)

poly1 = GF2Polynomial([1, 0, 1])
poly2 = GF2Polynomial([1, 1])

result = poly1 * poly2
print("Result of multiplication:", result)

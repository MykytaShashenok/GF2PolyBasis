import numpy as np
from dotenv import load_dotenv
import os

load_dotenv()

generator_coeffs_str = os.getenv('GENERATOR_POLYNOMIAL')
generator_coeffs     = np.array(eval(os.getenv("GENERATOR_POLYNOMIAL")), dtype=np.int8)
#generator_polynomial = GF2Polynomial(generator_coeffs)

class GF2Polynomial:
    def __init__(self, coeffs):
        self.coeffs = np.array(coeffs, dtype=np.int8) & 1
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
        return self.reduce(result_coeffs)

    def square(self):
        squared_coeffs = np.zeros(2 * len(self.coeffs) - 1, dtype=np.int8)
        squared_coeffs[::2] = self.coeffs
        return self.reduce(squared_coeffs)

    def reduce(self, coeffs):
        while len(coeffs) >= len(generator_polynomial.coeffs):
            if coeffs[0] == 1:
                coeffs[:len(generator_polynomial.coeffs)] ^= generator_polynomial.coeffs
            coeffs = np.trim_zeros(coeffs, 'f')
            if coeffs.size == 0:
                coeffs = np.array([0], dtype=np.int8)
        return GF2Polynomial(coeffs)

    def __repr__(self):
        return f"GF2Polynomial({self.coeffs.tolist()})"
    
    def power(self, exp):
        result = GF2Polynomial([1])
        base = self
        
        while exp > 0:
            if exp % 2 == 1:
                result = result * base
            base = base.square()
            exp //= 2
        
        return result
    
    def trace(self) :
        # just need to summarize powers of 2 
        pass

generator_polynomial = GF2Polynomial(generator_coeffs)
# generator_coeffs_str = os.getenv('GENERATOR_POLYNOMIAL')
# generator_coeffs = np.array(eval(os.getenv("GENERATOR_POLYNOMIAL")), dtype=np.int8)
# generator_polynomial = GF2Polynomial(generator_coeffs)

# poly = GF2Polynomial([1, 1, 1])
# squared_result = poly.square()
# squared_result_multiply = poly * poly
# power_result = poly.power(2**491 - 2)

# print("Result of squaring:", squared_result)
# print("Result of squaring (multiplication):", squared_result_multiply)
# print("Result of raising to the power of 2^251:", power_result)

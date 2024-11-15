import os
from dotenv import load_dotenv
from poly import GF2Polynomial
import numpy as np

load_dotenv()

generator_coeffs_str = os.getenv('GENERATOR_POLYNOMIAL')
generator_coeffs     = np.array(eval(generator_coeffs_str), dtype=np.int8)
generator_polynomial = GF2Polynomial(generator_coeffs)

def main():
    poly = GF2Polynomial([1, 1, 1])

    squared_result = poly.square()
    squared_result_multiply = poly * poly
    power_result = poly.power(2**491 - 2)

    print("Result of squaring:", squared_result)
    print("Result of squaring (multiplication):", squared_result_multiply)
    print("Result of raising to the power of 2^491 - 2:", power_result)

if __name__ == "__main__":
    main()

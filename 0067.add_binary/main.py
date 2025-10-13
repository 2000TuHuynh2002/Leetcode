class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_decimal = int(a, 2)
        b_decimal = int(b, 2)

        result_decimal = a_decimal + b_decimal
        result_binary = bin(result_decimal)

        return result_binary[2:]

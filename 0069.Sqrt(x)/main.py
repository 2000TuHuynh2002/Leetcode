class Solution:
    def mySqrt(self, x: int) -> int:
        result = 0

        while (1):
            if result*result > x:
                break
            result += 1

        return result - 1

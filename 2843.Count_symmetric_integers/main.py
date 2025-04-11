class Solution:
    def is_symmetric(self, n: int) -> bool:
        s = str(n)
        if len(s) % 2 != 0:
            return False
        sum_first_half = sum(int(digit) for digit in s[:len(s)//2])
        sum_second_half = sum(int(digit) for digit in s[len(s)//2:])
        return sum_first_half == sum_second_half

    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0
        for i in range(low, high + 1):
            if self.is_symmetric(i):
                count += 1
        return count

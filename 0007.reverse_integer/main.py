class Solution:
    def reverse(self, x: int) -> int:
        range_min = -2**31
        range_max = 2**31 - 1
        x_str = str(abs(x))
        x_str_reversed = x_str[::-1]

        if x >= 0:
            result = int(x_str_reversed)
        else:
            result = -int(x_str_reversed)

        if result < range_min or result > range_max:
            return 0
        else:
            return result

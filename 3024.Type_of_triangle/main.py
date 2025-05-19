class Solution:
    def triangleType(self, nums: List[int]) -> str:
        check = len(set(nums))
        sum_3_sides = sum(nums)

        for i in nums:
            if i >= sum_3_sides - i:
                return "none"

        if check == 1:
            return "equilateral"

        if check == 2:
            return "isosceles"

        return "scalene"

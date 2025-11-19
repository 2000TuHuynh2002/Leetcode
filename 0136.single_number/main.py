class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums_stack = []
        for num in nums:
            if num in nums_stack:
                nums_stack.remove(num)
            else:
                nums_stack.append(num)
        return nums_stack[0]

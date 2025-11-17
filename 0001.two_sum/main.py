class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx, _ in enumerate(nums):
            i = 1
            while idx + i < len(nums):
                if nums[idx] + nums[idx + i] == target:
                    return [idx, idx + i]
                i += 1

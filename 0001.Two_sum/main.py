class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]

        """
        
        for idx, num in enumerate(nums):
            i = 1
            while idx+i < len(nums):
                if nums[idx]+nums[idx+i] == target:
                    return [idx, idx+i]
                i += 1

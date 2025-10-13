class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        if nums[-1] - nums[0] >= 0:
            nums_copy = sorted(nums)
            return nums_copy == nums
        else:
            nums_copy = sorted(nums, reverse=True)
            return nums_copy == nums
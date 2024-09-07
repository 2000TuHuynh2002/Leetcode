class Solution:
    def findLengthOfLCIS(self, nums) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        
        count = 1
        max_count = 1
        range_nums = len(nums) - 1
        for i in range(range_nums):
            if nums[i+1] - nums[i] > 0:
                count += 1
                if count > max_count:
                    max_count = count
            else: 
                count = 1
        return max_count
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        remaining_idx = 0

        for i in range(0, len(nums)):
            if nums[i] != val:
                nums[remaining_idx] = nums[i]
                remaining_idx += 1

        return remaining_idx

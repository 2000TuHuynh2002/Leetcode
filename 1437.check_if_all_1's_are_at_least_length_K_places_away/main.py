class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        flat = 0
        count = 0

        for num in nums:
            if num == 1 and flat == 1 and count < k:
                return False

            if num == 1:
                flat = 1
                count = 0
            else:
                count += 1

        return True

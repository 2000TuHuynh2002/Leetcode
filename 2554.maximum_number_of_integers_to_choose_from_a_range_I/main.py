class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        # Use set for faster lookup
        banned = set(banned)
        result_count = 0
        temp_sum = 0

        for idx in range(1, n + 1):
            if idx in banned:
                continue

            temp_sum += idx
            if temp_sum > maxSum:
                break
            else:
                result_count += 1

        return result_count

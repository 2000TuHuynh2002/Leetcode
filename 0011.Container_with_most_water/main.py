class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Two pointers approach
        left = 0
        right = len(height) - 1
        result = 0

        while left < right:
            width = right - left
            min_height = min(height[left], height[right])
            area = width * min_height
            result = max(result, area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return result

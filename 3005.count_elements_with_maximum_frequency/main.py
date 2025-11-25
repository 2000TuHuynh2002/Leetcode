class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        num_dict = {}
        max_freq_count = 0

        for num in nums:
            try:
                num_dict[num] += 1
            except:
                num_dict[num] = 1

        max_val = max(num_dict.values())

        for n in num_dict.values():
            if n == max_val:
                max_freq_count += max_val

        return max_freq_count

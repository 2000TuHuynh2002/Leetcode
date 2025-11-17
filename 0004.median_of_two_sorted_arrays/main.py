class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        num = nums1 + nums2
        num.sort()
        num_len = len(num)

        if num_len % 2 != 0:
            return num[num_len // 2]
        else:
            return (num[int(num_len / 2)] + num[int(num_len / 2 - 1)]) / 2

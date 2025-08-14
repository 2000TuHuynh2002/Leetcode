class Solution:
    def largestGoodInteger(self, num: str) -> str:
        result = []
        for i in range(len(num)-2):
            if num[i] == num[i+1] and num[i+1] == num[i+2]:
                result.append(num[i])
        if result:
            return max(result)*3
        else:
            return ""

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ''.join(str(x) for x in digits)
        s = list(str(int(s) + 1))
        res = [eval(i) for i in s]
        return res

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        s = ''.join(str(x) for x in digits)
        s = list(str(int(s)+1))
        res = [eval(i) for i in s]
        return res

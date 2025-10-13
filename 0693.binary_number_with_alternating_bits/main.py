class Solution:
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """

        new = bin(n)[2:]
        for i in range(len(new) - 1):
            if new[i] == new[i+1]:
                return False
        return True

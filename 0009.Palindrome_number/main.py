class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        y = str(x)
        check=0
        for i in range(int(len(y)/2)):
            if y[i]==y[len(y)-1-i]:
                check+=1
        if check==int(len(y)/2):
            return True
        else: 
            return False
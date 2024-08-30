class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        roman2int = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000, 'IV':-2, 'IX':-2, 'XL':-20, 'XC':-20, 'CD':-200, 'CM':-200}
        num = 0
        for key, value in roman2int.items():
            num+=s.count(key)*value
        return num
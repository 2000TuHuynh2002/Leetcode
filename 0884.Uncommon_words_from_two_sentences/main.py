class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: List[str]
        """

        new_list = s1.split() + s2.split()
        result = []

        for char in new_list:
            if new_list.count(char) == 1:
                result.append(char)

        return result

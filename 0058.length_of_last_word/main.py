class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word_begin = 0
        word_len = 0

        for char in reversed(s):
            if char != " " and word_begin == 0:
                word_begin += 1
                word_len += 1
            elif char != " " and word_begin == 1:
                word_len += 1
            elif char == " " and word_begin == 1:
                return word_len

        return word_len

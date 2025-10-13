class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        str2_idx = 0
        str2_len = len(str2)

        for char1 in str1:
            if str2_idx < str2_len and (ord(str2[str2_idx]) - ord(char1)) % 26 < 2:
                str2_idx += 1

        return str2_idx == str2_len

class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""
        max_length = 0

        for i in range(len(s)):
            # Odd-length palindromes
            left, right = i, i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > max_length:
                    max_length = right - left + 1
                    result = s[left:right + 1]
                left -= 1
                right += 1

            # Even-length palindromes
            left, right = i, i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > max_length:
                    max_length = right - left + 1
                    result = s[left:right + 1]
                left -= 1
                right += 1

        return result

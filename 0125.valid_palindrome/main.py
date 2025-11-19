import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_string = re.sub(r'[^A-Za-z0-9]', '', s)
        lower_cleaned_string = cleaned_string.lower()
        return lower_cleaned_string == lower_cleaned_string[::-1]

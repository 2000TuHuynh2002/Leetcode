class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        excel_gap = 26

        for char in columnTitle:
            result = result * excel_gap + (ord(char) - ord("A") + 1)

        return result

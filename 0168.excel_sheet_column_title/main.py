class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = []
        while (columnNumber > 0):
            columnNumber -= 1
            # Explaination: 0 means A, 1 means B, 2 means C...
            result.append(chr(columnNumber % 26 + ord('A')))
            # That is why we should minus 1 before the conversion process
            columnNumber //= 26
        return ''.join(result[::-1])

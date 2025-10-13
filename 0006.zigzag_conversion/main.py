class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Create a list to hold the rows
        # For example, n=3, s="PAYPALISHIRING"
        # rows = [''] * n -> ['','','']
        #
        # The result after looping through the string:
        # rows = ['PAHN', 'APLSIIG', 'YIR']
        #
        # The final result would be "PAHNAPLSIIGYIR"

        rows = [''] * numRows
        curr_row = 0
        step = 1

        if numRows == 1 or numRows >= len(s):
            return s

        for char in s:
            rows[curr_row] += char

            if curr_row == 0:
                step = 1
            elif curr_row == numRows - 1:
                step = -1

            curr_row += step

        rows = ''.join(rows)
        return rows

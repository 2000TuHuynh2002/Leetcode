class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        count = 0 
        rows = len(mat)
        columns = len(mat[0])

        for row in range(rows):
            if sum(mat[row]) != 1:
                continue
            for column in range(columns):
                temp_sum = 0
                if mat[row][column] != 1:
                    continue
                for row2 in range(rows):
                    temp_sum += mat[row2][column]
                if temp_sum == 1:
                    count +=1
        return count
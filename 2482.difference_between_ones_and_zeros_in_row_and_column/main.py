class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        onesRow = []
        onesCol = []
        zerosRow = []
        zerosCol = []
        rows = len(grid)
        cols = len(grid[0])

        for cow in grid:
            onesRow.append(cow.count(1))
            zerosRow.append(cow.count(0))

        for col in range(cols):
            count_zero = 0
            count_one = 0

            for row in range(rows):
                if grid[row][col] == 0:
                    count_zero += 1
                elif grid[row][col] == 1:
                    count_one += 1

            zerosCol.append(count_zero)
            onesCol.append(count_one)

        diff = []
        for i in range(rows):
            temp = []
            for j in range(cols):
                temp.append(onesRow[i] + onesCol[j] - zerosRow[i] - zerosCol[j])
            diff.append(temp)

        return diff

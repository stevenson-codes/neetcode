class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])

        zeroRow, zeroCol = [False] * ROWS, [False] * COLS

        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    zeroRow[r] = True
                    zeroCol[c] = True
        
        for r in range(ROWS):
            for c in range(COLS):
                if zeroRow[r] or zeroCol[c]:
                    matrix[r][c] = 0
        

                    

        
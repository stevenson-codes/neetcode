class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])

        for i in range(ROWS >> 1):
            matrix[i], matrix[ROWS - 1 - i] = matrix[ROWS - 1 - i], matrix[i]
        for i in range(ROWS):
            for j in range(i, ROWS):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

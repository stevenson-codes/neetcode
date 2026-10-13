class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        rowSets = [set() for _ in range(n)]
        colSets = [set() for _ in range(n)]
        gridSets = [set() for _ in range(n)]

        for r in range(n):
            for c in range(n):
                if board[r][c] == '.':
                    continue
                num = board[r][c]
                if num in rowSets[r]:
                    return False
                if num in colSets[c]:
                    return False
                if num in gridSets[3 * (r // 3) + (c // 3)]:
                    return False
                rowSets[r].add(num)
                colSets[c].add(num)
                gridSets[3 * (r // 3) + (c // 3)].add(num)
        return True
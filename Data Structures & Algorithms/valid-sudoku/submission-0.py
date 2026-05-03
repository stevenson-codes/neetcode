class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        grids = defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board)):
                if board[r][c] != '.':
                    grid = (c // 3) + (r // 3) * 3
                    if board[r][c] in rows[r]:
                        return False
                    elif board[r][c] in cols[c]:
                        return False
                    elif board[r][c] in grids[grid]:
                        return False
                    rows[r].add(board[r][c])
                    cols[c].add(board[r][c])
                    grids[grid].add(board[r][c])
        return True
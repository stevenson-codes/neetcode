class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        posDiag = set()
        negDiag = set()

        board = [['.'] * n for _ in range(n)]
        res = []

        def bt(r):
            if r == n:
                res.append(["".join(board[i]) for i in range(n)])
                return
            
            for c in range(n):
                if c in cols or r + c in posDiag or r - c in negDiag:
                    continue
                
                cols.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                board[r][c] = 'Q'
                bt(r + 1)

                cols.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                board[r][c] = '.'
        
        bt(0)
        return res

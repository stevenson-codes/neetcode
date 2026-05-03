class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        ROWS, COLS = len(board), len(board[0])

        def dfs(row, col, index):
            if index == len(word):
                return True
            
            if (row < 0 or col < 0 or
                row >= ROWS or col >= COLS or
                (row, col) in visited or
                board[row][col] != word[index]):
                return False
            
            visited.add((row, col))
            
            res = (dfs(row + 1, col, index + 1) or
                  dfs(row - 1, col, index + 1) or
                  dfs(row, col + 1, index + 1) or
                  dfs(row, col - 1, index + 1))
            
            visited.remove((row, col))
            return res
        
        for i in range(ROWS):
            for j in range(COLS):
                if dfs(i, j, 0):
                    return True
        return False
            
                
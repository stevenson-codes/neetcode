class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def dfs(row, col):
            if (row < 0 or col < 0 or row == ROWS or col == COLS or
                grid[row][col] == 0):
                return 0
            grid[row][col] = 0
            size = 0
            for dr, dc in DIRS:
                size += dfs(row + dr, col + dc)
            return size + 1
        
        maxSize = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    maxSize = max(dfs(r, c), maxSize)
        return maxSize
            
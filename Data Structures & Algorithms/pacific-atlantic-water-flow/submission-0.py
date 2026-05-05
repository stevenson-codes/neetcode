class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pcf, atl = set(), set()
        ROWS, COLS = len(heights), len(heights[0])
        DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(row, col, visited, prevHeight):
            if (row < 0 or col < 0 or row == ROWS or col == COLS or
                (row, col) in visited or
                heights[row][col] < prevHeight):
                return
            
            visited.add((row, col))
            for dr, dc in DIRS:
                dfs(row + dr, col + dc, visited, heights[row][col])

        for r in range(ROWS):
            dfs(r, 0, pcf, heights[r][0])
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])
        
        for c in range(COLS):
            dfs(0, c, pcf, heights[0][c])
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])
        
        res = []
        for pos in pcf:
            if pos in atl:
                res.append(list(pos))
        return res
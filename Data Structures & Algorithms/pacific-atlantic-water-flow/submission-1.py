class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])

        pcf, atl = set(), set()

        def dfs(r, c, visited, prevHeight):
            if (r < 0 or c < 0 or r == ROWS or c == COLS or
                (r, c) in visited or
                heights[r][c] < prevHeight):
                return
            
            visited.add((r, c))
            dfs(r + 1, c, visited, heights[r][c])
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])
    
        for row in range(ROWS):
            dfs(row, 0, pcf, heights[row][0])
            dfs(row, COLS - 1, atl, heights[row][COLS - 1])
        
        for col in range(COLS):
            dfs(0, col, pcf, heights[0][col])
            dfs(ROWS - 1, col, atl, heights[ROWS - 1][col])
        
        res = []
        for pos in pcf:
            if pos in atl:
                res.append(pos)
        return res


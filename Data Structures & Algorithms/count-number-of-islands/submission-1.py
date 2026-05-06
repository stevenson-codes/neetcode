class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res, visited = 0, set()
        ROWS, COLS = len(grid), len(grid[0])
        DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def bfs(row, col):
            queue = deque()
            queue.append((row, col))

            while queue:
                row, col = queue.popleft()
                visited.add((row, col))
                for dr, dc in DIRS:
                    r, c = row + dr, col + dc
                    if (min(r, c) >= 0 and
                        r < ROWS and c < COLS and
                        grid[r][c] == "1" and
                        (r, c) not in visited):
                        queue.append((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in visited and grid[r][c] == "1":
                    res += 1
                    bfs(r, c)
        
        return res

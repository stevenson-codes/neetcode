class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = set()
        def bfs(row, col):
            queue = deque()
            queue.append((row, col))
            visited.add((row, col))
            count = 1
            while queue:
                row, col = queue.popleft()
                for dr, dc in DIRS:
                    r, c = row + dr, col + dc
                    if (min(r, c) >= 0 and r < ROWS and c < COLS and
                        grid[r][c] == 1 and
                        (r, c) not in visited):
                        visited.add((r, c))
                        count += 1
                        queue.append((r, c))
            return count
        
        maxSize = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    maxSize = max(bfs(r, c), maxSize)
        return maxSize
            
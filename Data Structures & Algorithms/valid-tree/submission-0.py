class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        edgeMap = defaultdict(list)
        for a, b in edges:
            edgeMap[a].append(b)
            edgeMap[b].append(a)
        
        visited = set()
        def bfs(index):
            queue = deque([(index, -1)])
            visited.add(index)
            while queue:
                i, par = queue.popleft()
                for neighbor in edgeMap[i]:
                    if neighbor in visited and neighbor != par:
                        return False
                    elif neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, i))
            return n == len(visited)

        return bfs(0)
        
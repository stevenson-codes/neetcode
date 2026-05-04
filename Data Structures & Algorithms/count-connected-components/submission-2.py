class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        count, visited = 0, set()

        hashmap = defaultdict(list)
        for edge in edges:
            a, b = edge
            hashmap[a].append(b)
            hashmap[b].append(a)
        
        def bfs(index):
            queue = deque([index])
            visited.add(index)
            while queue:
                i = queue.popleft()
                for neighbor in hashmap[i]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
                

        for i in range(n):
            if i not in visited:
                count += 1
                bfs(i)
        return count
            
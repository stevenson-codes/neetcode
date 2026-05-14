class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adjList = defaultdict(list)
        for i in range(len(points)):
            xi, yi = points[i]
            for j in range(i + 1, len(points)):
                xj, yj = points[j]
                dist = abs(xi - xj) + abs(yi - yj)
                adjList[i].append((dist, j))
                adjList[j].append((dist, i))
        
        res = 0
        visited = set()
        minHeap = [(0, 0)]
        while len(visited) < len(points):
            dist, point = heapq.heappop(minHeap)
            if point not in visited:
                visited.add(point)
                res += dist
                for cost, nei in adjList[point]:
                    if nei not in visited:
                        heapq.heappush(minHeap, (cost, nei))
        return res
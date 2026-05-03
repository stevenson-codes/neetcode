class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        minHeap = []
        for point in points:
            dist = (point[0]**2 + point[1]**2)**(1/2)
            heapq.heappush(minHeap, (dist, point))
        
        res = []
        for _ in range(k):
            res.append(heapq.heappop(minHeap)[1])
        
        return res
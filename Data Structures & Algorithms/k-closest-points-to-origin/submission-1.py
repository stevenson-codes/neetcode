class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        minHeap = []
        for point in points:
            dist = (point[0]**2 + point[1]**2)**0.5
            heapq.heappush(minHeap, [-dist, point])
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        return [point[1] for point in minHeap]
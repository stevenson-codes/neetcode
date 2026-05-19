class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        d = []
        res = []

        for x, y in points:
            dist = (x ** 2) + (y ** 2)
            d.append([dist, x, y])
        
        heapq.heapify(d)

        while (k > 0):
            dist, x, y = heapq.heappop(d)
            res.append([x, y])
            k -= 1

        return res
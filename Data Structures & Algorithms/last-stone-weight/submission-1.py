class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap = stones
        heapq.heapify_max(maxheap)

        while len(maxheap) > 1:
            stone1 = heapq.heappop_max(maxheap)
            stone2 = heapq.heappop_max(maxheap)
            if stone1 != stone2:
                heapq.heappush_max(maxheap, stone1 - stone2)
        maxheap.append(0)
        return maxheap[0]
            
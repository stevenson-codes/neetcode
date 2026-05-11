class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        heap = nums
        heapq.heapify(heap)

        for i in range(len(nums) + 1):
            if not heap or heapq.heappop(heap) != i:
                return i
        
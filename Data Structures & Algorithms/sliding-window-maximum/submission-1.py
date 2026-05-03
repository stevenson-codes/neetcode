class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res, queue = [], deque()
        
        for i in range(k):
            while queue and nums[queue[-1]] <= nums[i]:
                queue.pop()
            queue.append(i)
        
        res.append(nums[queue[0]])

        for r in range(k, len(nums)):
            while queue and nums[queue[-1]] <= nums[r]:
                queue.pop()
            queue.append(r)
            if queue[0] == r - k:
                queue.popleft()
            res.append(nums[queue[0]])
            print(queue)
        return res
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for n in nums:
            count[n] += 1
        
        bucket = [[] for _ in range(len(nums) + 1)]
        for n, c in count.items():
            bucket[c].append(n)
        
        res = sum(bucket, [])
        return res[-k:]

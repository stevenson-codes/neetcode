class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = defaultdict(int)
        for n in nums:
            count[n] += 1
        
        buckets = [[] for _ in range(len(nums) + 1)]
        for n, c in count.items():
            buckets[c].append(n)
        
        frequent = []
        for l in buckets:
            frequent += l
        
        return frequent[-k:]
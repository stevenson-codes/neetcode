class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        buckets = [[] for _ in range(len(nums) + 1)]
        count = {}
        res = []

        for n in nums:
            count[n] = count.get(n, 0) + 1
        
        for num, freq in count.items():
            buckets[freq].append(num)

        for i in range(0, len(buckets)):
            if buckets[i] != []:
                res += buckets[i]

        return res[-k:]
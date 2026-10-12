class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for _ in range(len(nums) + 1)]
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        
        for num in count:
            bucket[count[num]] += [num]
        
        res = []
        for i in range(len(bucket) - 1, -1, -1):
            for num in bucket[i]:
                res += [num]
                if len(res) == k:
                    return res
        return []

        
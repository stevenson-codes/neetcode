class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_map = {}
        for n in nums:
            num_map[n] = num_map.get(n, 0) + 1

        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in num_map.items():
            buckets[freq].append(num)

        freq = []
        for i in range(len(buckets) -1, 0, -1):
            if buckets[i] != []:
                freq += buckets[i]

        return freq[:k]

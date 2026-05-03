class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numbers = set(nums)
        dic = {}
        for num in numbers:
            dic[num] = nums.count(num)

        freq = sorted(dic, key=lambda num : dic[num], reverse=True)
        return freq[:k]

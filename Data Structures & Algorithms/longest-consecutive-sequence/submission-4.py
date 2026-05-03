class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numSet = set(nums)
        res = 0
        for n in numSet:
            if n - 1 not in numSet:
                i = 1
                while n + i in numSet:
                    i += 1
                res = max(i, res)
        return res
                
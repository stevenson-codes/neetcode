class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique = set(nums)
        count = 0

        for n in nums:
            if n - 1 not in nums:
                i = 1
                while n + i in nums:
                    i += 1
                count = max(count, i)
        
        return count
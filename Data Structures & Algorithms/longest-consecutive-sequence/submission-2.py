class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique = list(set(nums))

        res = 0
        for n in unique:
            if n - 1 not in unique:
                count = 1
                while n + count in unique:
                    count += 1
                res = max(res, count)
        return res


            
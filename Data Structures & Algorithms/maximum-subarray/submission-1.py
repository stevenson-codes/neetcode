class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum, res = 0, float('-inf')
        for n in nums:
            sum += n
            res = max(res, sum)
            if sum < 0:
                sum = 0
        return res
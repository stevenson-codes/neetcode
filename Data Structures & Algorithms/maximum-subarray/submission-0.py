class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum, res = 0, float('-inf')
        for n in nums:
            if sum < 0 and sum < n:
                sum = n
            else:
                sum += n
            res = max(res, sum)
        return res
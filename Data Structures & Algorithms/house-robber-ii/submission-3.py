class Solution:
    def rob(self, nums: List[int]) -> int:
        def dp(nums):
            rob1, rob2 = 0, 0
            for n in nums:
                rob1, rob2 = rob2, max(n + rob1, rob2)
            return rob2

        if len(nums) < 2:
            return nums[0]
        return max(dp(nums[1:]), dp(nums[:-1]))
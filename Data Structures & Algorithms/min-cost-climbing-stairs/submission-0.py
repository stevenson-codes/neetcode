class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [101] * (len(cost) + 2)
        dp[-1] = 0
        dp[-2] = 0

        for i in range(len(cost) - 1, -1, -1):
            dp[i] = cost[i] + min(dp[i + 1], dp[i + 2])
        
        return min(dp[0], dp[1])

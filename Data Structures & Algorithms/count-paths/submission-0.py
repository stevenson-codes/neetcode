class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                curr = 0
                if i - 1 >= 0:
                    curr += dp[i - 1][j]
                if j - 1 >= 0:
                    curr += dp[i][j - 1]
                dp[i][j] += curr
        return dp[-1][-1]
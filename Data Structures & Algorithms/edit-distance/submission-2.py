class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)

        dp = [[float('inf')] * (n + 1) for _ in range(m + 1)]

        for r in range(m + 1):
            dp[r][n] = m - r

        for c in range(n + 1):
            dp[m][c] = n - c
        
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if word2[i] == word1[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    dp[i][j] = 1 + min(dp[i][j + 1], dp[i + 1][j], dp[i + 1][j + 1])
        return dp[0][0]
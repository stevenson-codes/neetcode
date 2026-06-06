class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s))
        dp.append(True)

        for i in range(len(s) - 1, -1, -1):
            for word in wordDict:
                if not dp[i] and s[i:].startswith(word):
                    dp[i] = dp[i + len(word)] 

        print(dp)
        return dp[0]
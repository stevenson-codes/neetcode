class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, res = 0, 0
        charSet = {}

        for r in range(len(s)):
            if s[r] in charSet:
                l = max(charSet[s[r]] + 1, l)
            charSet[s[r]] = r
            res = max(res, r - l + 1)

        return res


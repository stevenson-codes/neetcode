class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = {}
        l, res = 0, 0
        for r in range(len(s)):
            if s[r] in charSet:
                l = max(l, charSet[s[r]] + 1)
            charSet[s[r]] = r
            res = max(res, r - l + 1)
        return res
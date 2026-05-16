class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res, l = 0, 0
        idxMap = {}
        for r in range(len(s)):
            if s[r] in idxMap:
                l = max(l, idxMap[s[r]])
            idxMap[s[r]] = r + 1
            res = max(res, r - l + 1)
        return res

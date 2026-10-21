class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        res = 0
        count = defaultdict(int)

        for r in range(len(s)):
            count[s[r]] += 1
            while count[s[r]] > 1:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res
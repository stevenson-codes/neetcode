class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, res = 0, 0
        maxCount = 0
        counter = defaultdict(int)

        for r in range(len(s)):
            counter[s[r]] += 1
            maxCount = max(maxCount, counter[s[r]])

            while r - l + 1 - maxCount > k:
                counter[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res
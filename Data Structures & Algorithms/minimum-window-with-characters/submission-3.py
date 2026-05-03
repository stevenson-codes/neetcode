class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        count = defaultdict(int)
        for c in t:
            count[c] -= 1

        length = len(s)
        res = ""
        have, need = 0, len(count)

        l = 0
        for r in range(len(s)):
            if s[r] in count:
                count[s[r]] += 1
                if count[s[r]] == 0:
                    have += 1
            while have == need:
                if length >= r - l + 1:
                    res = s[l:r + 1]
                    length = r - l + 1
                if s[l] in count:
                    count[s[l]] -= 1
                    if count[s[l]] == -1:
                        have -= 1
                l += 1
            print(res, s[l:r + 1], length)
        return res
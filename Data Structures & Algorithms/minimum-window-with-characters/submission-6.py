class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counter = defaultdict(int)
        for c in t:
            counter[c] += 1
        
        has, need = 0, len(counter)
        l, res, rstr = 0, len(s), ''
        for r in range(len(s)):
            if s[r] in counter:
                counter[s[r]] -= 1
                if counter[s[r]] == 0:
                    has += 1
            
            while has == need:
                if res >= r - l + 1:
                    rstr = s[l:r + 1]
                    res = r - l + 1
                if s[l] in counter:
                    counter[s[l]] += 1
                    if counter[s[l]] == 1:
                        has -= 1
                l += 1
        return rstr


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        a1 = defaultdict(int)
        a2 = defaultdict(int)

        for i in range(len(s)):
            a1[s[i]] += 1
            a2[t[i]] += 1
        
        return a1 == a2
            
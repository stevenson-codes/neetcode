class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        perm = Counter(s1)
        l, r = 0, len(s1) - 1
        while l < len(s2):
            if s2[l] in s1:
                if Counter(s2[l:l + len(s1)]) == perm:
                    return True 
            l += 1
        return False
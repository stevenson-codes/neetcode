class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            res += str(len(s)) + '@' + s
        return res

    def decode(self, s: str) -> List[str]:
        l = 0
        res = []
        while l < len(s):
            r = l
            while s[r] != '@':
                r += 1
            length = int(s[l:r])
            r += 1
            res.append(s[r:r + length])
            l = r + length
    
        return res



class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + '@' + s
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        
        i = 0
        res = []
        while i < len(s):
            lenS = ''
            while s[i] != '@':
                lenS += s[i]
                i += 1
            i += 1
            res.append(s[i:i + int(lenS)])
            i += int(lenS)
        return res

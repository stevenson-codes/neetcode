class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + '&' + s
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            j = i
            while s[j] != '&':
                j += 1
            l = int(s[i:j])
            j += 1
            res.append(s[j:j + l])
            i = j + l
        return res
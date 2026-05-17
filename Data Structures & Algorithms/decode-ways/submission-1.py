class Solution:
    def numDecodings(self, s: str) -> int:
        w1, w2 = 1, 0

        for i in range(len(s) - 1, -1, -1):
            tmp = 0
            if s[i] != '0':
                tmp = w1
            
            if i + 1 < len(s) and (s[i] == '1' or s[i] == '2' and s[i + 1] in '0123456'):
                tmp += w2
            w1, w2 = tmp, w1
            
        return w1


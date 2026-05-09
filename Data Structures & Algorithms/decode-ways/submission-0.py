class Solution:
    def numDecodings(self, s: str) -> int:
        way1, way2 = 1, 0
        n = len(s)

        for i in range(n - 1, -1 , -1):
            curr = 0
            if s[i] != '0':
                curr = way1
            if i + 1 < n and (s[i] == '1' or (s[i] == '2' and s[i + 1] in '0123456')):
                curr += way2
            way1, way2 = curr, way1
        return way1
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        w1, w2 = 2, 1
        for i in range(2, n):
            tmp = w1
            w1 = w1 + w2
            w2 = tmp
        return w1
        
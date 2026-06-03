class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def minHours(piles, rate):
            res = 0
            for pile in piles:
                res += -(pile // -rate)
            return res
        
        l, r = 1, max(piles)
        while l < r:
            m = (l + r) // 2
            hours = minHours(piles, m)
            if hours > h:
                l = m + 1
            else:
                r = m
        return l
            
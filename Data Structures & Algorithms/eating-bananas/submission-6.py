class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def eatingSpeed(rate):
            hours = 0
            for pile in piles:
                hours += -(pile // -rate)
            return hours
        
        l, r = 1, max(piles)
        while l < r:
            m = (l + r) // 2
            if eatingSpeed(m) <= h:
                r = m
            else:
                l = m + 1
        return l
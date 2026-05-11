class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        res = []
        count = 0
        for inter in intervals:
            if res and res[-1][1] > inter[0]:
                count += 1
                res[-1][1] = min(res[-1][1], inter[1])
            else:
                res.append(inter)
        return count
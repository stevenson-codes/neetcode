class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        prevEnd = intervals[0][1]
        count = 0
        for inter in intervals[1:]:
            if prevEnd > inter[0]:
                count += 1
                prevEnd = min(prevEnd, inter[1])
            else:
                prevEnd = inter[1]
        return count
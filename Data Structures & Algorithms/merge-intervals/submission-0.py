class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]

        for inter in intervals:
            curr = res[-1]
            if curr[1] >= inter[0]:
                curr[1] = max(curr[1], inter[1])
            else:
                res.append(inter)
        return res

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0 for _ in range(len(temperatures))]
        for i, t in enumerate(temperatures):
            count = 1
            while stack and stack[-1][0] < t:
                temp, idx = stack.pop()
                res[idx] = i - idx
            stack.append((t, i))
        return res


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxRectangle = 0
        stack = []
        for i, h in enumerate(heights):
            idx = i
            while stack and stack[-1][1] >= h:
                idx, height = stack.pop()
                maxRectangle = max(maxRectangle, height * (i - idx))
            stack.append((idx, h))
        
        for i, h in stack:
            maxRectangle = max(maxRectangle, h * (len(heights) - i))
        
        return maxRectangle

            
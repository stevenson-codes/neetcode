class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxRectangle = 0
        stack = []
        for i, h in enumerate(heights):
            if not stack or h >= stack[-1][1]:
                stack.append((i, h))
            else:
                idx = i
                while stack and stack[-1][1] >= h:
                    idx, height = stack.pop()
                    maxRectangle = max(maxRectangle, height * (i - idx))
                stack.append((idx, h))
            print(stack)
        
        for i, h in stack:
            maxRectangle = max(maxRectangle, h * (len(heights) - i))
        
        return maxRectangle

            
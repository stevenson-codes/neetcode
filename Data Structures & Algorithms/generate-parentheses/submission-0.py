class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []

        def dfs(leftCount, rightCount):
            if leftCount == rightCount == n:
                res.append("".join(stack))

            if leftCount < n:
                stack.append("(")
                dfs(leftCount + 1, rightCount)
                stack.pop()
            
            if leftCount > rightCount:
                stack.append(")")
                dfs(leftCount, rightCount + 1)
                stack.pop()
        
        dfs(0, 0)
        return res
            
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def maxPath(root):
            if not root:
                return 0
            left = maxPath(root.left)
            right = maxPath(root.right)
            path = root.val + max(left, right)
            return max(path, 0)
        
        def dfs(root):
            nonlocal res
            if not root:
                return 0
            curPath = maxPath(root.right) + root.val + maxPath(root.left)
            res = max(res, curPath)

            dfs(root.left)
            dfs(root.right)

        res = float('-inf')
        dfs(root)
        return res
        

        

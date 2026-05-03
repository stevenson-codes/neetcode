# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return 0, True
            
            left, b_left = dfs(root.left)
            right, b_right = dfs(root.right)

            if (left - right) <= 1 and (left - right) >= -1:
                return 1 + max(left, right), b_left and b_right
            else:
                return 1 + max(left, right), False
        return dfs(root)[1]
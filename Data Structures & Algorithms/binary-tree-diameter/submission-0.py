# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(root, res):
            if not root:
                return (0, 0)

            left, resl = dfs(root.left, res)
            right, resr = dfs(root.right, res)
            res = max(resl, resr, left + right, res)

            return (1 + max(left, right), res)

        return dfs(root, 0)[1]

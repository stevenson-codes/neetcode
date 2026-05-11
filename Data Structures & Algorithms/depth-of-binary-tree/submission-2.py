# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        queue = deque([root])
        depth = 0

        while queue:
            children = []
            for node in queue:
                if node.left:
                    children.append(node.left)
                if node.right:
                    children.append(node.right)
            depth += 1
            queue = deque(children)
        return depth
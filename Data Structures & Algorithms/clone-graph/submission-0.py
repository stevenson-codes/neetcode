"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {}

        def dfs(curr):
            if not curr or curr in oldToNew:
                return
            
            oldToNew[curr] = Node(curr.val)
            for neighbor in curr.neighbors:
                dfs(neighbor)
                oldToNew[curr].neighbors.append(oldToNew[neighbor])
            
            return oldToNew[curr]
            
        clone = dfs(node)
        return clone
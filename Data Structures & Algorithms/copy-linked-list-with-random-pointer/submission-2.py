"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        nodes = {}
        res = Node(0)
        curr = res
        while head:
            if head in nodes:
                curr.next = nodes[head]
            else:
                curr.next = Node(head.val)
                nodes[head] = curr.next
            
            curr = curr.next
            if not head.random:
                curr.random = None
            else:
                if head.random in nodes:
                    curr.random = nodes[head.random]
                else:
                    curr.random = Node(head.random.val)
                    nodes[head.random] = curr.random
            head = head.next
            
        return res.next



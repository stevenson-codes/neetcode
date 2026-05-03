# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        dummy, cur = ListNode(), head
        while cur:
            if cur.next == dummy:
                return True
            next = cur.next
            cur.next = dummy
            cur = next
        return False
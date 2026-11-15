# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        curr = head
        for _ in range(n):
            curr = curr.next
        
        front = dummy
        while curr:
            curr = curr.next
            front = front.next
        
        front.next = front.next.next
        return dummy.next

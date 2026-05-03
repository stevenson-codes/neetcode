# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def reverseList(head):
            prev = None
            curr = head

            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            return prev

        
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        head2 = reverseList(slow.next)
        slow.next = None
        head1 = head

        while head1 and head2:
            next1 = head1.next
            next2 = head2.next

            head1.next = head2
            head2.next = next1

            head1 = next1
            head2 = next2

            
        


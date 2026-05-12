# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        curr = slow.next
        slow.next = None

        # Reverse right list
        prev = None
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        right = prev
        left = head
        while right:
            nextLeft = left.next
            left.next = right

            nextRight = right.next
            right.next = nextLeft

            right = nextRight
            left = nextLeft
        


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        curr = res

        acc, carry = 0, 0
        while l1 or l2:
            a, b = 0, 0
            if l1:
                a = l1.val
                l1 = l1.next
            if l2:
                b = l2.val
                l2 = l2.next

            acc = a + b + carry
            carry = acc > 9
            curr.next = ListNode(acc % 10)
            
            curr = curr.next

        
        curr.next = ListNode(1) if carry else None
        
        return res.next

            

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        list1, list2 = head, slow.next
        slow.next = None

        prev = None
        while list2:
            tmp = list2.next
            list2.next = prev
            prev = list2
            list2 = tmp
        list2 = prev
        

        while list1 and list2:
            tmp1, tmp2 = list1.next, list2.next
            list1.next = list2
            list2.next = tmp1
            list1, list2 = tmp1, tmp2
        
        


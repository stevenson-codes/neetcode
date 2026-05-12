# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Wrapper:
    def __init__(self, node):
        self.node = node
    
    def __lt__(self, other):
        return self.node.val < other.node.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for l in lists:
            heapq.heappush(heap, Wrapper(l))
        
        res = ListNode()

        curr = res
        while heap:
            wrapper = heapq.heappop(heap)
            curr.next = wrapper.node
            curr = curr.next

            if wrapper.node.next:
                heapq.heappush(heap, Wrapper(wrapper.node.next))
        return res.next

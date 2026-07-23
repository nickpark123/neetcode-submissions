# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        s = set()
        if not head or not head.next:
            return False

        while head.next:
            if head.next in s:
                return True
            else: 
                s.add(head.next)
                head = head.next
                
        return False   




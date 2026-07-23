# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        t = head
        front = head
        end = head

        for i in range(n):
            end = end.next

        if not end:
            return head.next
        
        while end.next:
            front = front.next
            end = end.next

        delete = front.next

        if not delete.next:
            front.next = None
        else:
            front.next = delete.next
            
        return t





































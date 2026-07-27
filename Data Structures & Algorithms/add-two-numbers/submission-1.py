# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    
        solution = ListNode()
        cur = solution
        remainder = 0

        while l1 or l2 or remainder != 0:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            if v1 + v2 + remainder < 10:
                g = v1 + v2 + remainder
                remainder = 0
            else:
                g = (v1 + v2 + remainder) % 10
                remainder = 1

            solution.next = ListNode(g)
            solution = solution.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return cur.next











            

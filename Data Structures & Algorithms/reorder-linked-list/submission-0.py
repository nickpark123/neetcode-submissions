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
        
        second = slow.next
        slow.next = None
        prev = None
        while second:
            temp = second.next #1, temp = 2, 3, 4
            second.next = prev #make 1's next none
            prev = second # make 1 the prev
            second = temp

        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1

            first = tmp1
            second = tmp2


        
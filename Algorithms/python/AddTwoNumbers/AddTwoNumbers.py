# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1 = ''
        for i in l1:
            s1 += str(l1.pop())

        s2 = ''
        for i in range(len(l2)):
            s2 += str(l2.pop())

        return list(str(int(s1) + int(s2))[::-1])
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        temp = head
        temp_list = ''
        while temp:
            temp_list += str(temp.val)
            temp = temp.next
        return temp_list == temp_list[::-1]
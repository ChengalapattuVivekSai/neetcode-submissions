# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None

        while curr:
            temp = curr.next #storing the temp value for the current next
            curr.next = prev
            prev = curr
            curr = temp #here we will pass the value direclty to temp

        return prev #new head of reversed linked list
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev=None
        curr=head

        while curr is not None:
            next = curr.next
            print(next)
            curr.next = prev
            prev = curr
            print(prev)
            curr = next
            print(curr)

        return prev
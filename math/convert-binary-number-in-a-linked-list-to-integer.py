# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        dummy=head
        current=dummy 
        string=""

        while current :
            string+=str(current.val)
            current = current.next
        ans=int(string, 2)
        return ans



        
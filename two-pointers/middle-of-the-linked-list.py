# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        current=head
        count=0
            
        while current:
            count+=1
            # prev=current
            current=current.next
        # if count%2==0:
        middle=count//2+1
            # print(middle)
        # elif count%2!=0: # count = 6
        #     middle=(count//2)+1 # count // 2 + 1
            # print(middle)

        current=head

        for _ in range(0, int(middle-1)):
            current=current.next
            # print(current.value)
            
        return current
            
        
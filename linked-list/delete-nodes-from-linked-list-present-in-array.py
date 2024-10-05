# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        
        j=ListNode(0)
        
        lis=j
        new=head
        while new:
            
            if new.val not in nums:
                lis.next = ListNode(new.val)  
                lis = lis.next 
            new=new.next
        return j.next   

                #     continue
                # else:
                #     lis.append(j)
                # new=nex
                # position+=1
        
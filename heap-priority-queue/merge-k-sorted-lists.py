# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if not lists:
            return None

        list1 = lists[0]

        for i in range(1, len(lists)):  
            list2 = lists[i]

            dummy=ListNode()
            tail=dummy
            while list1 and list2:
                if list1.val<list2.val:
                    tail.next=list1
                    list1=list1.next
                else:
                    tail.next=list2
                    list2=list2.next
                tail=tail.next
           
            tail.next = list1 if list1 else list2
            list1 = dummy.next

        return list1

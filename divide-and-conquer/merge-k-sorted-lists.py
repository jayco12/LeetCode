# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        for i in range(len(lists)):

            list2=lists[i]
            list1 = lists[i - 1]

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
            if list1:
                tail.next=list1
            else:
                tail.next=list2
            return dummy.next

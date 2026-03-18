# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        self.list1=list1
        self.list2=list2
        merged=sorted(self.list1 +self.list2)
        print(merged) 
rnn=Solution()
rnn.mergeTwoLists([43,4,4,43,43,55,55],[23,3,4,53,4,2,43])

        
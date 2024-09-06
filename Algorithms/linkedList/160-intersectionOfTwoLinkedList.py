# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        pOne = headA
        pTwo = headB

        while pOne != pTwo:
            pOne = pOne.next if pOne else headB
            pTwo = pTwo.next if pTwo else headA
        
        return pOne 
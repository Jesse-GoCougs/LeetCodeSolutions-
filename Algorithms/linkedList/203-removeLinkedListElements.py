# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        current = head 
        #node to remove is at the head of list 
        while current and current.val == val:
            current = current.next
        
        prev, output = current, current

        #node to remove is in the middle of the list or end 
        while current:
            if current.val == val:
                prev.next = current.next 
            else:
                prev = current
            current = current.next
        
    
        return output 
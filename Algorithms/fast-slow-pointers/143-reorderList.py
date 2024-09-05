# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        """
        1. find the middle of the list
        2. reverse second half of list 
        3. use head and tail pointer (that now points to the end of the list in reverse order) to merge both list in alternate order 
        """
        if not head or not head.next:
            return

        middleNode = self.findMiddle(head)
        secondHalf = self.reverseList(middleNode.next)
        middleNode.next = None  # This splits the list into two halves

        firstHalf = head

        while firstHalf and secondHalf:
            # Save next pointers
            tmp1 = firstHalf.next
            tmp2 = secondHalf.next

            # Reorder pointers
            firstHalf.next = secondHalf
            secondHalf.next = tmp1

            # Move to the next nodes in the list
            firstHalf = tmp1
            secondHalf = tmp2

    def findMiddle(self, head):
        slow = head 
        fast = head 

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next 

        return slow 

    def reverseList(self, head):
        current = head
        previous = None  # Corrected from null to None

        while current:
            next_node = current.next  # Use a temporary variable to store the next node
            current.next = previous 
            previous = current 
            current = next_node

        return previous

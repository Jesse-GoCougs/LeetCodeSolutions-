# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    """
      Steps 
      1. find the middle node 
      2. reverse the second half of the list 
      3. now iterate both pointer head and tail and compare 
      4. reverse second half of list to original form if valid palindrome 
    """
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return True
        
        mid = self.findMiddleOfList(head)
        second_half = self.reverseList(mid)

        first_half = head
        while second_half:
            if first_half.val != second_half.val:
                return False
            first_half = first_half.next
            second_half = second_half.next

        # Restore the list (optional)
        mid.next = self.reverseList(mid.next)

        return True

    def findMiddleOfList(self, head):
        slow = head
        fast = head 
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow 

    def reverseList(self, head):
        previous = None
        current = head
        while current:
            current = head.next
            head.next = previous
            previous = head
            head = current
        return previous
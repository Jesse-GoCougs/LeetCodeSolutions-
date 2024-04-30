def reverseBetween(head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        # Dummy node to handle edge cases where left = 1
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        for _ in range(left - 1):
            prev = prev.next

        # Reverse the sublist from left to right
        current = prev.next
        sublist_tail = current
        prev.next = None  # Terminate the sublist
        for _ in range(right - left + 1):
            next_node = current.next
            current.next = prev.next
            prev.next = current
            current = next_node

        # Connect the reversed sublist with the rest of the list
        sublist_tail.next = current

        return dummy.next
def main():
# Call the function you want to run
     input1 = [1,2,3,4,5]
     reverseBetween(input1, 2, 4)
 


# Execute the main function
if __name__ == "__main__":
    main()
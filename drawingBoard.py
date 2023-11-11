# def reverseString(s):
#     if len(s) <=1:
#         return s
#     return reverseString(s[1:]) + s[0]
# def isPalindrome(s):
#     if len(s) <= 1:
#         return True 
#     return isPalindrome(s[1:-1]) if s[0] == s[-1] else False  

# def decimalToBinary(n, result):
#     if n == 0:
#         return result
#     result = str(n%2) + result
#     return decimalToBinary(n //2, result)
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def reverse_linked_list(head):
    # Base case: if head is None or the last node, return head
    if head is None or head.next is None:
        return head

    # Recursively reverse the rest of the linked list
    reversed_list_head = reverse_linked_list(head.next)

    # Reverse the links (changing pointers)
    head.next.next = head
    head.next = None

    return reversed_list_head

# Helper function to print the reversed linked list
def print_linked_list(node):
    while node:
        print(node.value, end=" -> " if node.next else " -> None\n")
        node = node.next



def main():
# Call the function you want to run
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)

    reverseHead = reverse_linked_list(head)
    print_linked_list(reverseHead)

# Execute the main function
if __name__ == "__main__":
    main()



"""
Solution Summary:

"""
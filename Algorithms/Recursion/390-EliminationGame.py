
def lastRemaining(n: int) -> int:
    left = True  # flag to keep track of left-to-right or right-to-left elimination
    remaining = n  # keep track of the remaining numbers
    step = 1  # keep track of the step size
    head = 1  # keep track of the head of the remaining numbers
    while remaining > 1:
        # if we're going from left to right or from right to left with an odd number of remaining elements
        # or from right to left with an even number of remaining elements, then we need to update the head
        if left or remaining % 2 == 1:
            head += step
        step *= 2  # double the step size
        remaining //= 2  # divide the remaining elements by 2
        left = not left  # flip the flag

    return head


def main():
# Call the function you want to run
    print(lastRemaining(9))


# Execute the main function
if __name__ == "__main__":
    main()



"""
Solution Summary:
     We can solve this problem by keeping a few things in mind. We need to keep track of the size of the current space or n at each iteration. 
     So for example with input n=9 size is 9 initially but we will decrease the size by half each time since we will remove n/2 
     elements each turn. Additionally, we simply want to keep track of the head element of the array each time since we will 
     return the head when size of array is equal to 1 which is our conditional statement to stop. 

     Now for cases when n%2 == 0 or in other words n is even we need to remove the head since if we are moving from left to right.

     For our second condition where n % 2 ==1 or n is odd we will have two cases 
        if n is even: we will not remove the head 
        if n is odd we will remove the head 

    so we can combine the two cases when we are moving left to right (flag == true) or (flag == false and n is odd) we update the head for both these cases
    otherwise we dont so we simply update our step size and divide our remaining by half and change our flag to opposite

    so we keep doing these steps above until our remaining size n is equal to 1.

    This solution runs in O(n) time and uses no space 

    This is a clever solution keep in mind for future problems. 
"""
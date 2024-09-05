def longestConsecutive(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    unique = set(nums)
    longestSequence = 0

    for number in unique:
        if number-1 not in unique: # this is the start of a new sequence 
            sequence = 0         #ex. [1,2,3] if 0 not in set 1 is the start of a sequence
            currenentSequence = number
            while currenentSequence in unique:
                sequence += 1
                currenentSequence += 1
            longestSequence = max(sequence, longestSequence)
    return longestSequence 



def main():
    nums = [100,4,200,1,3,2]
    # Output: 4
    # Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. 
    # Therefore its length is 4.
    print(longestConsecutive(nums))


# Execute the main function
if __name__ == "__main__":
    main()



"""
Solution Summary:
    This Problem is a leetcode hard difficulty, but once we break the problem down into
    smaller steps we can easily solve it effienciently. The problem gives us an unsorted array 
    of numbers and wants us to find the longest consective sequence of the input numbers. 
    
    My first thought process was we can sort the array and then just iterate over our sorted list 
    and keep track of the longest consecutive sequence. The problem with doing this is that sorting 
    the array takes o(nlogn) time complexity and the problem wants us to solve this problem in linear time
    also sorting the array first defeats the purpose of the question being hard difficulty. 

    The otherway we can do this and is how we solved it above is by placing our numbers into 
    a set or a dict. And then finding the numbers that are the start of a sequence 
    (single numbers are still a sequence of 1)

    For the example below we have 3 different sequences with the longest one being length 4 

    ex. [100,4,200,1,3,2]

        100
        1->2->3->4
        200

    we can find the start of each of the sequences by using our set, we can check if 
    for the current number (current - 1) is in our set if so then it is not the start of a sequence 
    otherwise the number is the start of a sequence. 

    We can find all of the start of a sequence within our input list numbers and then keep iterating 
    over our set as long as (current +1) is in the set. Once this condition is broken we simply compare our 
    longest varible with the current sequence length and update it. 

    We keep doing this until we reach the end of our input list.

    This algorithm has 

    Time Complexity:O(n)
    Space Compelxity: O(n)


"""
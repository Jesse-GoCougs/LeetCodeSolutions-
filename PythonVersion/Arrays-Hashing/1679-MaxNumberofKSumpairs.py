from collections import defaultdict
def maxOperations(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    table = defaultdict(int)
    operations = 0

    for num in nums:
        x = k - num
        if x in table:
            operations +=1
            table[x] -= 1

            if table[x] <= 0:
                del table[x]
        else: 
            table[num] += 1
    return operations
    


# #template Code 


def main():
# Call the function you want to run
    nums = [2,5,4,4,1,3,4,4,1,4,4,1,2,1,2,2,3,2,4,2]
    print(maxOperations(nums, 3))


# Execute the main function
if __name__ == "__main__":
    main()



"""
Solution Summary:

"""    
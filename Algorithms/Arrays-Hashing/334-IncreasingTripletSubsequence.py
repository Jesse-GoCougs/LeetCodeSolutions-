
# def increasingTriplet(nums):
#     """
#     :type nums: List[int]
#     :rtype: bool
#     """
#     n = len(nums)
#     if n < 3:
#         return False

#     prefixMin = [1] * n 
#     postfixMax = [1] * n

#     currentMin = nums[0]
#     currentMax = nums[-1]

#     for index, num in enumerate(nums):
#         prefixMin[index] = currentMin
#         currentMin = min(currentMin, num)
    
#     for index in range(n-1, -1, -1):
#         postfixMax[index] = currentMax
#         currentMax = max(currentMax, nums[index])

#     for index in range(1, len(nums)-1):
#         if nums[index] > prefixMin[index] and nums[index] < postfixMax[index]:
#             return True 
#     return False
import sys 
def increasingTriplet(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    first = sys.maxsize
    second = sys.maxsize

    for num in nums:
        if num <= first:
            first = num
        elif num <= second:
            second = num
        else:
            return True 
    return False

def main():
# Call the function you want to run
    nums = [1,2,3,4,5]
    print(increasingTriplet(nums))


# Execute the main function
if __name__ == "__main__":
    main()



"""
Solution Summary:

"""
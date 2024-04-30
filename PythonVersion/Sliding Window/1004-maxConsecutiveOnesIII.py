def longestOnes(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    left = 0
    right = 0
    longest = 0

    while right < len(nums):
        if nums[right] == 0 and k < 0:
            #move our left pointer until and update k 
            #do this until we have a valid k value 
            while nums[left] == 1 and left <= right:
                left += 1
            left += 1
            k += 1
        elif nums[right] == 0:
            k -= 1
        longest = max(left + (right - left), longest)
        right +=1
    return longest

def main():
# Call the function you want to run
    nums = [1,1,1,0,0,0,1,1,1,1,0]
    k = 2
    print(longestOnes(nums, k ))

# Execute the main function
if __name__ == "__main__":
    main()



"""
Solution Summary:

"""
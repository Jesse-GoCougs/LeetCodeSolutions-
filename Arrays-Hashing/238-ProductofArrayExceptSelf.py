def productExceptSelf(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    res = [1] * (len(nums))

    prefix = 1
    for i in range(len(nums)):
        res[i] = prefix
        prefix *= nums[i]
    postfix = 1
    for i in range(len(nums) - 1, -1, -1):
        res[i] *= postfix
        postfix *= nums[i]
    return res




def main():
# Call the function you want to run
    nums = [1,2,3,4]
    print(productExceptSelf(nums))


# Execute the main function
if __name__ == "__main__":
    main()



"""
Solution Summary:
 This problem is tricky to think about especially givin the constraints they gave us in which we cant use the 
 division which would in turn make this problem extremely easy to solve. 

 IF we want the product of the array expcept for the current element we can think of this 
 in a more programming perspective. Essentially we want the product of all the elements to the left 
 of the array and the product of all the elements to the right of the array and multiply them with 
 each other for each element. 
 So we could have two pointers that for each element they move left and move right and compute the 
 total product for each of these elements. This algorithm would take us O(n^2) time. But we can also simply just 
 precomute the prefix sum for the elements in the array and the postfix sum for each element in the array and 
 store them in 2 different array and then use the "index" to grab the left prefix and the right postfix for each element 
 (left prefix * right postfix) and that would be the total we are looking for. This algorithm works and runs in O(n) time but 
 it does take O(n) space as well. 


 We can improve this by not using the space to store the prefix and postfix for each element. 
 Instead we can compute those numbers and store them in our output array directly then just multiply the corresponding 
 values with each other in our output array. Which is exactly what we did in the above solution. 
 So the solution above has a 

    Space Complexity: (1)
    Time Complexity: O(n)

    Since we are no longer using the space to store prefix and postfix


"""
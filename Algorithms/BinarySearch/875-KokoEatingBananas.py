import math
def minEatingSpeed(piles, h):
    """
    :type piles: List[int]
    :type h: int
    :rtype: int
    """
    output = max(piles)
    left = 1
    right = output

    while left <= right:
        mid = (left + right) // 2
        total = 0
        for curr in piles:
            total += math.ceil(float(curr) / mid)
        if total <= h:
            output = mid
            right = mid -1
        else:
            left = mid+1
    return output
def main():
# Call the function you want to run
    piles = [3,6,7,11]
    h = 8
    # Output: 4
    print(minEatingSpeed(piles, h))


# Execute the main function
if __name__ == "__main__":
    main()



"""
Solution Summary:
This problem is solved using a binary search technique. We start by anaylzying the problem and the information they give us initially 
We are told that koko wants to be able to finish eating all her banannas in <= h time. And we want to be able to find the minimum amount of banannas she can eat 
in h time and still be able to finish all of them in time. 
    . h >= len(piles) since we need to be able to finish all of the banannas in time 
    . max amount of bannanas she can eat is max(piles)
    . if k > piles[i] then we eat piles[i] banannas for that hr and cant eat beyond that for that hr 

Given the information we have above we can come up with a brute force approach for each pile of banannas we can eat at most 
max(piles) and we can eat min of 1 bananna per hr or in other words we can eat 
    1...max(piles) per hr our job is to find the minimum number in this series that is a valid nuber of banannas we can eat per hr 
since we can have multiple numbers (k) values that are valid we have to continue doing this until we reach a valid min number "k"

We can of course check all of the numbers in this series but we can also come up with a better time complecity by using the 
binary search technique to narrow our choices down each time. 

Time Complexity: O(log(max(p)) * p)
Space Complexity: O(n)

"""
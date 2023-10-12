def trap(height):
    """
    :type height: List[int]
    :rtype: int
    """

    #calculater the count of all bars in between two points and sum them up 
    def calculateBars(left, right, height):
        total = 0
        while left < right:
            if height[left] > 0:
                total += height[left]
            left += 1
        return total
    
    #calculate total area in between left and right pointers
    def calculateArea(left, right, height):
        y = min(height[left], height[right])
        x = right - (left + 1)
        area = x * y
        bars = calculateBars(left + 1, right, height)
        return area - bars

    #start of actual function 
    n = len(height)
    left = 0
    waterTotal = 0

    while left < n:
        if height[left] > 0:
            right = left + 1
            secondMax = 0
            secondMaxIndex = 0

            #look for matching size bar or bigger
            while right < n and height[right] < height[left]:
                if height[right] > secondMax:
                    secondMax = height[right]
                    secondMaxIndex = right
                right += 1

            if right < n:# found matching size bar or bigger calcualte area
                print("pairs: (", left, ", ", right, ")")
                waterTotal += calculateArea(left, right, height)
                left = right
            elif secondMax > 0: # no matching size bar found use second biggest and calculate area
                print("pairs 2: (", left, ", ", secondMaxIndex, ")")
                waterTotal += calculateArea(left, secondMaxIndex, height)
                left = secondMaxIndex 
            else:
                left +=1
        else: # left pointer has no bar bigger than 0 so we increment 
            left += 1
    return waterTotal
def main():
# Call the function you want to run
    test1 = [0,1,0,2,1,0,1,3,2,1,2,1]
    test2= [4,2,0,3,2,5]
    test3 = [4,2,3]
    print("output: ", trap(test1))
    print("output 2: ", trap(test2))
    print("output 3: ", trap(test3))


# Execute the main function
if __name__ == "__main__":
    main()
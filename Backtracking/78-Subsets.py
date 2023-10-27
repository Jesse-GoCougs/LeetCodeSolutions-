def generateSubsets(nums):
    def backtrack(start, current_subset):
        # Add the current subset to the result
        result.append(current_subset[:])

        # Explore all choices for the remaining elements
        for i in range(start, len(nums)):
            current_subset.append(nums[i])  # Include the current element
            backtrack(i + 1, current_subset)  # Recursively explore with the element included
            current_subset.pop()  # Exclude the current element (backtrack)

    result = []
    backtrack(0, [])  # Start from index 0 with an empty subset
    return result


def main():
# Call the function you want to run
    # Example usage with input [5, 1, 6]
    input_array = [5, 1, 6]
    subsets = generateSubsets(input_array)

    for subset in subsets:
        print(subset)


# Execute the main function
if __name__ == "__main__":
    main()

"""
Solution Summary:
    We approached this problem using a backtracking technique. We want to generate all subsets of the input array. 
    We know that thier will be 2^n total possible subsets. Since for each element we can have 2 choices 
        1. We add the element to our current subset
        2. We dont add the element to our current subset
    The way this problem is solved above is we start with the empty subset and call our function we first append the empty subset and 
    then we iterate over each of our elements and add it to our current set. Then we backtrack or recurse all the way down our tree 
    adding elements into our subset each time until we reach a leaf node then we backtrack and pop the last set off 
    then we continue this process until we explored all possible paths and created all the possible subsets. 
    Think of this problem as using a tree and exploring each path. The time complexity of a backtracking solution is 
    exponential 

    O(2^n)

"""
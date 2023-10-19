def groupAnagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """

    grouped = {}
    
    for word in strs:
        sorted_word = ''.join(sorted(word))  # Convert the string to a list and sort it
        if sorted_word in grouped:
            grouped[sorted_word].append(word)
        else:
            grouped[sorted_word] = [word]
    
    return grouped.values()



def main():
# Call the function you want to run
    # Example 1:
    strs = ["eat","tea","tan","ate","nat","bat"]
    # Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
    # Example 2:

    strs2 = [""]
    # Output: [[""]]
    # Example 3:

    strs3 = ["a"]
    # Output: [["a"]]
    print(groupAnagrams(strs))
    print(groupAnagrams(strs2))
    print(groupAnagrams(strs3))



# Execute the main function
if __name__ == "__main__":
    main()



"""
Solution Summary:
    This problem is similar to the previous problem we solved isAnagram() in which we checked if the given strings were anagrams of each other 
    recall that the way we solved this is by using 2 dictionaries to check for frequency of the characters in each string and if they were both equal 
    we would keep a counter called matches that would keep track of the number of matches we would have in the end of the iterarion over our string. 
    Then we would simply compare our macthes variable with our 1st counter length and return True if they were equal false otherwise. 

    The difference with this problem is that we have more than just one string to compare and check if it is am anagram. 
    So we can take a different approach. We can sort all of our strings and store the newly sorted string in a dictionary with the sorted string being the key in our dict. 
    Then since we have all of our strings sorted we can check if the current sorted string is in our dict if so we would map our unsorted string to the sorted key value in our dict and add 
    it to the values list for that key. We keep doing this for the rest of the input strings and then 
    we simply return a list of all the values in our dict. 

    Time Complexity:O(nlogn) since we need to sort the strings in our input list first 
    Space Complexity:O(n) since at worst case we will have n values stored in our dict 
"""
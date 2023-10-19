from collections import Counter
from heapq import heappop, heappush


def topKFrequent(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    table = Counter(nums)
    minHeap = []

    for key, val in table.items():
        heappush(minHeap, (val, key))
        if len(minHeap) > k:
            heappop(minHeap)
    return [tup[1] for tup in minHeap]

def main():
# Call the function you want to run
    print()


# Execute the main function
if __name__ == "__main__":
    main()



"""
Solution Summary:

    We can solve this problem in multiple ways the brute force approach is to use a dictionary or a counter 
    to count the frequencies for each of our characters, then we would use our dicr or counter and find the "max" or most frequent 
    element in our dict and add it to our output list, we would do this "k" times. 
    ALthough this would techniqually work the fact that we would have to find the max each time and update our dict 
    would be time consumming especially for large k values.

    The approach we took instead was to add our elements into a counter to keep track of the frequencies of our characaters. Then 
    we iterate over our counter and add these values into a minheap with the values being stored as tuples 
    with ("val", "freqency"). Since python does not have  max heap we use a minheap and we instead add a check 
    to see if the minheap length is larger than k. If so we pop from our heap we keep doing this until we iterate over all of our values in our 
    counter. Then we simply return a list of all the values in our min heap. Which is the kth largest elemensts since we poped all our smaller values 
    and only left k values in our heap which is all of the large values. 

    Time complexity: O((n * log(k))
    Space Complexity: O(n)


    




    Explained 

**Time Complexity:**

1. Counting the frequency of each element in `nums` using `Counter(nums)`
 takes O(n) time, where n is the length of the `nums` list.

2. Building the min-heap (`heappush`) and maintaining it as a min-heap with 
at most `k` elements takes O(n * log(k)) time. For each element in `nums`,
 you perform a constant amount of work for push and pop operations in the heap.

3. Constructing the result list from the min-heap takes O(k * log(k)) time 
since you pop the `k` smallest elements from the heap.

The dominant term in terms of time complexity is O(n * log(k)), where 
`n` is the length of `nums` and `k` is the value passed as a parameter. 
The code is efficient because it reduces the number of elements in the
 heap to `k`, making it suitable for cases where `k` is much smaller 
 than the total number of unique elements in `nums`.

**Space Complexity:**

1. The `table` dictionary created by `Counter(nums)` stores the frequency 
of each element, which takes O(n) space.

2. The `minHeap` is used to store a maximum of `k` elements. In the worst case, 
if `k` is equal to the number of unique elements in `nums`, it will take O(k) space.
 However, in most practical scenarios, `k` is much smaller than the number of unique 
 elements in `nums`.

The space complexity is O(n) for the `table` dictionary and O(k) for 
the `minHeap`, where `k` is the value you pass as a parameter. 
The space complexity is dominated by the dictionary in this case.

In summary, the time complexity of this code is O(n * log(k)), 
and the space complexity is O(n) for the frequency dictionary and O(k) 
for the min-heap. The actual performance depends on the specific values of 
`n` and `k` in your input data.

"""
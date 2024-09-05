class Solution(object):
    def maxScore(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: int
        """
        #pair the elements from nums1 and nums2 and sort based on nums2 in decending order
        pairs = sorted(zip(nums2, nums1), reverse = True)

        #minheap to maintain top k elements from nums1
        min_heap = []
        sum_k_elements = 0
        max_score = 0

        for i in range(len(nums1)):
            num2, num1 = pairs[i]

            #add the current element from nums1 into the heap
            heapq.heappush(min_heap, num1)
            sum_k_elements += num1

            #if the heap exceeds size k, remove the smallest element
            if len(min_heap) >k:
                sum_k_elements -= heapq.heappop(min_heap)

            # if the heap has exactly k elements, calculate the score 
            if len(min_heap) ==k:
                max_score = max(max_score, sum_k_elements * num2)

        return max_score
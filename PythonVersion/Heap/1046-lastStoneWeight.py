import heapq
class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        max_heap = [-item for item in stones]
        heapq.heapify(max_heap)

        while len(max_heap) >=2:
            val1 = -heapq.heappop(max_heap)
            val2 = -heapq.heappop(max_heap) 

            if val1 == val2:
                continue 
            new_val = val1-val2
            heapq.heappush(max_heap, -new_val)
       
            
        return -heapq.heappop(max_heap) if len(max_heap) >0 else 0 
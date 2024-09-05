import heapq

class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        rightMax = -1
        index = len(arr)-1
      
        while index >= 0 : 
            temp = arr[index]
            arr[index] = rightMax
            rightMax = max(rightMax, temp)
            index -=1

        return arr
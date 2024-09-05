class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)-1
        closest, index  = target, 0 
        left, right = 0, n 

        while left <= right:
            midpoint = (left + right)  // 2

            if nums[midpoint] == target:
                return midpoint
            
            #adjust our pointers now 
            if nums[midpoint] < target:
                left = midpoint +1
               
            else:
                right = midpoint-1

        return left
        
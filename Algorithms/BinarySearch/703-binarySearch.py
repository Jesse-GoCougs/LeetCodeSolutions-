class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0 
        right = len(nums)-1

        while left <= right:
            midPoint = (left + right) // 2
            current = nums[midPoint]
            if current == target:
                return midPoint
            elif current > target:
                right = midPoint -1
            elif current < target:
                left = midPoint +1
        return -1

        
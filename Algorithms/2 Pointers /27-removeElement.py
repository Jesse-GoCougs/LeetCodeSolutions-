class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        n = len(nums)
        left = 0

        for i in range(n):
            if nums[i] != val:
                nums[left] = nums[i]
                left +=1
        return left 
            
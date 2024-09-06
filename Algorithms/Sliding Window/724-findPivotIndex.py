
class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = sum(nums)
        currentSum = 0

        for index, curr in enumerate(nums):
            total -= curr 
            if currentSum == total:
                return index
            currentSum += curr
        return -1
            
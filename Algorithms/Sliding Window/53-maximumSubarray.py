class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        currentSum = 0
        totalSum = nums[0]

        for i in range(len(nums)):
            if currentSum < 0:
                currentSum = 0
            currentSum += nums[i]
            totalSum = max(currentSum, totalSum)
        return totalSum 
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = 0
        n = len(nums)
        num = 0
        for index in range(n):
            num ^= nums[index]
        return num
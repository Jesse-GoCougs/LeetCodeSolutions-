class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left = 0
        right = len(nums)-1
        output = list()

        while (left <= right):
            if abs(nums[left]) > abs(nums[right]):
                temp = pow(nums[left], 2)
                left+=1
            else:
                temp = pow(nums[right], 2)
                right-=1
            output.insert(0, temp)
        return output
            
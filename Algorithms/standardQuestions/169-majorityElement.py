class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        currentElement = nums[0]
        currentCount = 0

        for index in range(len(nums)):
            if nums[index] == currentElement:
                currentCount += 1
            elif nums[index] != currentElement and currentCount <= 0:
                currentElement = nums[index]
                currentCount = 1
            else:
                currentCount -= 1

        return currentElement 
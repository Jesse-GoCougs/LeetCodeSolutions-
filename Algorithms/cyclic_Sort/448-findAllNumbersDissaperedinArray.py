class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Place each number in its correct position
        index = 0
        while index < len(nums):
            currentVal = nums[index]
            correctIndex = currentVal - 1
            
            if nums[index] != nums[correctIndex]:
                # Swap values to their respective slot
                nums[index], nums[correctIndex] = nums[correctIndex], nums[index]
            else:
                index += 1
        
        # Now check to see which values are not in the correct slot if any
        output = []
        for i in range(len(nums)):
            if nums[i] != i + 1:
                output.append(i + 1)
                
        return output
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        visited = set()
        for i in range(len(nums)):
            if nums[i] not in visited:
                n = len(visited)
                if i > n:
                    nums[n] = nums[i]
                visited.add(nums[i])
            else:
                continue
        return len(visited)   

    #other solution that also works the same but whithout using the stack 
    # since the input array is already sorted 
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 1
        for right in range(1, len(nums)):
            if(nums[right]!=nums[right-1]):
                nums[left] = nums[right]
                left+=1
        return left
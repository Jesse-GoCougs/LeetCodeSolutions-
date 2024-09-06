class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        stack = []
        nextGreaterMap = {}

        for num in nums2:
            while stack and num > stack[-1]:
                smaller = stack.pop()
                nextGreaterMap[smaller] = num
            stack.append(num)
        while stack:
            current = stack.pop()
            nextGreaterMap[current] = -1

        return [nextGreaterMap[num] for num in nums1]
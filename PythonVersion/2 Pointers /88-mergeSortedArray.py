class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        
        left, right = m-1, n-1
        i = len(nums1)-1

        while left >=0 or right >=0:
            #compare both array values 
            if left >= 0 and right >= 0:
                if nums1[left] >= nums2[right]:
                    nums1[i] = nums1[left]
                    left-=1
                else:
                    nums1[i] = nums2[right]
                    right -=1
            else: # only add one array since we finished with other values 
                if left >=0:
                    nums1[i] = nums1[left]
                    left-=1
                else:
                    nums1[i] = nums2[right]
                    right -=1

            i -= 1
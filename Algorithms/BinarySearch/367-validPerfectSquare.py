class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        left = 0 
        right = num 

        while left <= right:
            mid = left + (right - left) // 2
            squared = mid * mid
            if squared == num:
                return True
            elif squared > num:
                right = mid-1
            elif squared < num:
                left = mid + 1
        return False


# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 0
        end = n

        while start <= end: 
            midPoint = (start + end )//2
            result = guess(midPoint)
            if result == 0:
                return midPoint
            elif result == -1:
                end = midPoint - 1
            else:
                start = midPoint + 1
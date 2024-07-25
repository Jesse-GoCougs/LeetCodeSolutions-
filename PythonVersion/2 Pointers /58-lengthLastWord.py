class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        right = len(s)-1

        while s[right] == ' ':
            right -=1
        left = right 
        while left >= 0 and s[left] != ' ':
            left -=1
            
        return (right - left)

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        lengthLast = 0
        for i in range(len(s)-1,-1,-1):
            if s[i] != ' ':
                lengthLast += 1
            elif lengthLast >0:
                break
        return lengthLast
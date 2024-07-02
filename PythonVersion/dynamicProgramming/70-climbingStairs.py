class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        numWays = [0] * n
        numWays[0], numWays[1] = 1,2
  
        for i in range(2,n):
            numWays[i] = numWays[i-1] + numWays[i-2]
        
        return numWays[n-1]
class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        completeSteps = 0
        counter  = 1

        while n >0 and counter <= n: 
            n = n - counter
            if n >=0:
                completeSteps +=1
            counter += 1 
        return completeSteps 
class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        binaryRep = []
        for i in range(n+1):
            binaryRep.append(self.findBinaryOnes(i))
        return binaryRep

    #convert to binary and return the number of ones in binary representation
    def findBinaryOnes(self, n):
        numOnes = 0
        remainder, divided = n,0
        
        while remainder > 0:
            divided = remainder % 2
            remainder /= 2
            if divided == 1:
                numOnes += 1
        return numOnes
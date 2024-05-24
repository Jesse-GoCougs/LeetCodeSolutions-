class Solution(object):
    def minFlips(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        aString, bString, cString = '{0:030b}'.format(a), '{0:030b}'.format(b), '{0:030b}'.format(c)
        count = 0
        n = len(cString)

        for index in range(n):
            if cString[index] == '1':
                if aString[index] != '1' and bString[index] != '1':
                    count += 1
            elif cString[index] =='0':
                if aString[index] == '1':
                    count +=1
                if bString[index] == '1':
                    count +=1
        return count 
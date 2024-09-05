

#solution number 1 we use the fast and slow pointer approach to find the loop 
# in this case find if number is happy or not 
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        slow = n
        fast = n

        while True:
            slow = self.calculateSumOfSqaures(slow)
            fast = self.calculateSumOfSqaures(self.calculateSumOfSqaures(fast))
            if slow == fast:
                break
        return slow == 1

    def calculateSumOfSqaures(self, number):
        total = 0
        for digit in str(number):
            total += int(digit) **2
        return total 

#Solution number 2 use a set to find if number is a happy number 
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        currentNumber = n
        visited = {currentNumber}

        while currentNumber != 1:
            currentNumber = self.calculateSumOfSqaures(currentNumber)
            if currentNumber in visited: #loop detected
                return False
            else:
                visited.add(currentNumber)

        return True 

    def calculateSumOfSqaures(self, number):
        total = 0
        for digit in str(number):
            total += int(digit) **2
        return total 
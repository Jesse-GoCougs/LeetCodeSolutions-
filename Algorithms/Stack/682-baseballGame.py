class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        stack = []
        for operation in operations:
            self.performOperation(operation, stack)

        totalScore = 0
        while stack:
            totalScore += stack.pop()
        return totalScore

    
    def performOperation(self, operation, stack):
        if operation == '+':
            val1 = stack.pop()
            val2 = stack.pop()
            sumVal = val1+val2

            stack.append(val2)
            stack.append(val1)
            stack.append(sumVal)
        elif operation == 'D':
            doubleScore = stack[-1] *2
            stack.append(doubleScore)
        elif operation == 'C':
            stack.pop()
        else:
            score = int(operation)
            stack.append(score)        
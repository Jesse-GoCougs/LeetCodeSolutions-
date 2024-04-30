class MinStack(object):

    def __init__(self):
        self.stack = []  # Initialize main stack as instance variable
        self.auxiliaryStack = []  # Initialize auxiliary stack as instance variable

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)

        # Now add to auxiliary stack
        if self.auxiliaryStack:
            if val <= self.auxiliaryStack[-1]:  # Use <= to handle duplicates
                self.auxiliaryStack.append(val)
        else:
            self.auxiliaryStack.append(val)

    def pop(self):
        """
        :rtype: None
        """
        if self.stack:
            element = self.stack.pop()
            if element == self.auxiliaryStack[-1]:
                self.auxiliaryStack.pop()

    def top(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        if self.auxiliaryStack:
            return self.auxiliaryStack[-1]
        
def main():
    print(":)")

    if __name__ == "__main__":
        main()
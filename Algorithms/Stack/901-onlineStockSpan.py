class StockSpanner(object):

    def __init__(self):
        self.stack = []

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        span = 1
        # Aggregate spans of all prices less than or equal to the current price
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]
        
        # Push the current price and its span to the stack
        self.stack.append((price, span))
        
        return span
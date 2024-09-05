from collections import deque

class RecentCounter:

    def __init__(self):
        self.requests = deque()

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        # Remove requests older than t - 3000
        while self.requests and self.requests[0] < t - 3000:
            self.requests.popleft()

        # Add the new request
        self.requests.append(t)

        # Return the number of requests within the last 3000 milliseconds
        return len(self.requests)
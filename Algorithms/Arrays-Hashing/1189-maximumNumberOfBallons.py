class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        # Correct spelling of "balloon"
        required = "balloon"
        counter = {}
        
        # Count the occurrences of each character in the text
        for char in text:
            if char in required:
                counter[char] = counter.get(char, 0) + 1
        
        # We need to count 'b', 'a', 'l', 'o', 'n'
        # 'l' and 'o' appear twice in the word "balloon"
        minCount = float('inf')
        
        # Check if all required characters are present
        for char in 'balon':
            if char in counter:
                if char == 'l' or char == 'o':
                    # Since 'l' and 'o' are needed twice in "balloon"
                    minCount = min(minCount, counter[char] // 2)
                else:
                    minCount = min(minCount, counter[char])
            else:
                # If any required character is missing, return 0
                return 0
        
        return minCount
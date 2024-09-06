class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        visited = set()
        mapping = dict()

        patternLength = len(pattern)
        words = s.split()
        wordCount = len(words)

        if patternLength != wordCount:
            return False

        for i in range(wordCount):
            currentPattern = pattern[i]
            currentWord = words[i]  # Corrected variable name

            if currentPattern in mapping:
                if mapping[currentPattern] != currentWord:  # Fixed condition
                    return False
            else:
                if currentWord in visited:
                    return False
                mapping[currentPattern] = currentWord
                visited.add(currentWord)
                
        return True
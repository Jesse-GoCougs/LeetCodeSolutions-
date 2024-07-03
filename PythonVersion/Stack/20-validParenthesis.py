class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = list()
        
        for current in s:
            if current == '(' or current == '{' or current == '[':
                stack.append(current)
            else:
                if current == ')' and stack:
                    if stack[-1] != '(':
                        return False
                elif current  == '}' and stack:
                     if stack[-1] != '{':
                        return False
                elif current == ']' and stack:
                     if stack[-1] != '[':
                        return False
                else:
                    return False
                stack.pop()
        return True if not stack else False
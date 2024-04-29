
def validPallindromeII(s):
    left = 0
    right = len(s)-1
    while left < right:
        if s[left] != s[right]:
            return isValidPallindrome(s, left+1, right) or isValidPallindrome(s, left, right-1)
        left +=1
        right -=1
    return True 

def isValidPallindrome(s, left , right):
    while left < right:
        if s[left] != s[right]:
            return False
        left +=1
        right -=1
    return True 

def main():
    input1 = "abccbda"
    input2 = "racecar"
    input3 = "abcdef"
    print(validPallindromeII(input1))
    print(validPallindromeII(input2))
    print(validPallindromeII(input3))


if __name__ == "__main__":
    main()
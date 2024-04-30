def minAddToMakeValid(S: str) -> int:
    balance = 0
    added = 0

    for char in S:
        if char == '(':
            balance += 1
        elif char == ')':
            if balance == 0:
                added += 1
            else:
                balance -= 1
    return added + balance

def main():
    input1 = "())"
    input2 = "))(("

   
    print(minAddToMakeValid(input1))
    print(minAddToMakeValid(input2))


if __name__ == "__main__":
    main()
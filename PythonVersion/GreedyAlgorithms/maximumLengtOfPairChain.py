def findLongestChain(pairs):
    """
    :type pairs: List[List[int]]
    :rtype: int
    """
    pairs.sort(key = lambda p: p[1])
    chainCount = 1
    previous = pairs[0][1]

    for current in pairs[1:]:
        if previous < current[0]:
            chainCount += 1
            previous = current[1] 
    return chainCount

def main():
    input1 = [[1,2],[2,3],[3,4]]
    input2 = [[1,2],[7,8],[4,5]]
   
    print(findLongestChain(input1))
    print(findLongestChain(input2))


if __name__ == "__main__":
    main()
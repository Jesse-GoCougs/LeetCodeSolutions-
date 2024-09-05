def readBinaryWatch(turnedOn):
    """
    :type turnedOn: int
    :rtype: List[str]
    """
    output = []

    for hrs in range(12):
        for min in range(60):
            temp = bin(hrs) + bin(min)
            if temp.count("1") == turnedOn:
                time = '%d:%02d' % (hrs,min)
                output.append(time)
    return output

def main():
# Call the function you want to run
    turnedOn = 1
    # Output: ["0:01","0:02","0:04","0:08","0:16","0:32","1:00","2:00","4:00","8:00"]
    print(readBinaryWatch(turnedOn))


# Execute the main function
if __name__ == "__main__":
    main()



"""
Solution Summary:
    This problem is a perfect example of using a backtracking algorithm. When we have a backtgracking approach to a problem 
    we need to think of 3 different ways in which we can use it either we want to find the optimal solution, find all possible viable solutions, or 
    find any valid solution. 

    When I think of backtracking I picture a state tree in which we continue down the tree until we find a valid solution if so we 
    add that solution and backtrack to our parent or vise versa for invalid solutions. Although, recurssion is ussually needed for 
    backtracking problems. In this case we dont need to use recurssion. Instead think how can I come up with all possible solutions and then 
    narrow my choices down to only valid ones (which will then be addded to my output array). In this case we can use two seperate for loops 
    to represent the hrs and the minutes. Then we convert each number to a binary representaion of that time and compare the number of 1's
    in our binary number to the number of "turnedOn" given to us as input. If they are equal that current time is a valid solution so we convert the binary to 
    a string with the valid time format i.e (1:03... 5:20) and then just add it to our outout array.

    This solution runs in exponential time since we have to check all possible solutions. 

    Note: We dont always have to use recurssion to solve a backtracking problem as long as we can compute all possible solutions 
    and narrow our choices down after. Although, for most other problems recussion is almost always used to simplfy the problem.  

"""
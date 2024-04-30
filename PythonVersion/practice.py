# from collections import Counter
# from heapq import heappop, heappush
def remove_duplicates(arr):
    # index of the next non-duplicate element
    next_non_duplicate = 1

    i = 0
    while(i < len(arr)):
      if arr[next_non_duplicate - 1] != arr[i]:
        arr[next_non_duplicate] = arr[i]
        next_non_duplicate += 1
      i += 1

    return next_non_duplicate


def main():
# Call the function you want to run
    test = [1, 1, 2, 2, 3, 3, 4, 4]
    print(remove_duplicates(test))


# Execute the main function
if __name__ == "__main__":
    main()
def linear_search(arr, target):
    # Your code here
    for i in arr:
        if i == target:
            return arr.index(i)

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    start = 0
    end = len(arr) - 1

    while start <= end:
        midpoint = start + (end - start) // 2
        if arr[midpoint] == target:
            return midpoint

        elif arr[midpoint] > target:
            end = midpoint - 1

        else:
            start = midpoint + 1


    return -1  # not found

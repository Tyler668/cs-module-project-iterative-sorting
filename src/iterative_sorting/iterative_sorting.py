# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(len(arr)):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        # while cur_index >= smallest_index:
        #     cur_index += 1
        # smallest_index = cur_index
        for j in range(cur_index + 1, len(arr)):
            if arr[smallest_index] > arr[j]:
                smallest_index = j              
                


        # TO-DO: swap
        # Your code here
        arr[smallest_index], arr[i] = arr[i], arr[smallest_index]


    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
    swaps = 0

    while swaps is not None:
        swaps = 0
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                swaps += 1
                arr[i], arr[i+1] = arr[i+1], arr[i]
        if swaps == 0:
            swaps = None



    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):
    # Your code here


    return arr

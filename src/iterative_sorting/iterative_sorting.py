# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for n in range(smallest_index+1, len(arr)):
            if arr[cur_index] > arr[n]:
                cur_index = n

        # TO-DO: swap
        arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    n = len(arr)
   # Traverse through all array elements
    for i in range(n):
            # Last i elements are already in correct position
        for j in range(0, n-i-1):
                # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    ############################################################################
    # for n in range(len(arr)-1, 0, -1):
    #     for i in range(n):
    #         if arr[i] > arr[i+1]:
    #             temp = arr[i]
    #             arr[i] = arr[i+1]
    #             arr[i+1] = temp
    ##############################################################################################
    # exchanges = True
    # passnum = len(arr)-1
    # while passnum > 0 and exchanges:
    #     exchanges = False
    #     for i in range(passnum):
    #         if arr[i] > arr[i+1]:
    #             exchanges = True
    #             temp = arr[i]
    #             arr[i] = arr[i+1]
    #             arr[i+1] = temp
    #     passnum = passnum-1
    return arr

    # STRETCH: implement the Count Sort function below


def count_sort(arr, maximum=-1):

    return arr

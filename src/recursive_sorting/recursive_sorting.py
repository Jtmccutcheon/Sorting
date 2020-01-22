# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # TO-DO
    # delcare indicies for each sublist
    a = 0
    b = 0
    for i in range(elements):
        # check if either list is empty if so append the other
        if a >= len(arrA):
            merged_arr[i] = arrB[b]
            b += 1
        elif b >= len(arrB):
            merged_arr[i] = arrA[a]
            a += 1
        # otherwise compare and append the smallest of the two
        elif arrA[a] < arrB[b]:
            merged_arr[i] = arrA[a]
            a += 1
        else:
            merged_arr[i] = arrB[b]
            b += 1

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TO-DO
    # check if length is 1 or less if so return list
    if len(arr) <= 1:
        return arr
    # divide in half
    left = arr[0:len(arr) // 2]
    right = arr[len(arr) // 2]
    # sort left
    merge_sort(left)  # bubble or quicksort can work here too
    # sort right
    merge_sort(right)
    # merge together
    return merge(left, right)


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr

"""
This script implements the merge sort
"""

import rand


def merge_sort(array):
    """merge sort the given arr

    Args:
        arr (list): the list to be sorted

    Returns:
        list: the sorted arr list
    """
    if len(array) <= 1:
        return array

    half = len(array) // 2

    return recombine(merge_sort(array[:half]), merge_sort(array[half:]))


def recombine(left_arr, right_arr):
    """Merges two sorted arrays into one sorted array.

    Args:
        leftArr (list): The first sorted list
        rightArr (list): The second sorted list

    Returns:
        list: The merged sorted list
    """
    left_index = 0
    right_index = 0
    merge_arr = [None] * (len(left_arr) + len(right_arr))
    while left_index < len(left_arr) and right_index < len(right_arr):
        if left_arr[left_index] < right_arr[right_index]:
            merge_arr[left_index + right_index] = left_arr[left_index]
            left_index += 1
        else:
            merge_arr[left_index + right_index] = right_arr[right_index]
            right_index += 1

    for i in range(right_index, len(right_arr)):
        merge_arr[left_index + right_index] = right_arr[i]
        right_index += 1

    for i in range(left_index, len(left_arr)):
        merge_arr[left_index + right_index] = left_arr[i]
        left_index += 1

    return merge_arr


arr = rand.random_array([None] * 20)
arr_out = merge_sort(arr)

print(arr_out)

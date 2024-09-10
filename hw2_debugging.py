"""
This is a script to implement merge sort
"""
import rand


def merge_sort(input_array):
    """
    Merge Sort Function
    """
    if len(input_array) == 1:
        return input_array

    half = len(input_array) // 2

    return recombine(merge_sort(input_array[:half]), merge_sort(input_array[half:]))


def recombine(left_arr, right_arr):
    """
    Recombine function, merge two sorted arrays
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
    
    while left_index < len(left_arr):
        merge_arr[left_index + right_index] = left_arr[left_index]
        left_index += 1
    while right_index < len(right_arr):
        merge_arr[left_index + right_index] = right_arr[right_index]
        right_index += 1
        
    return merge_arr


arr = rand.random_array([None] * 20)  # External 'arr' variable
arr_out = merge_sort(arr)

print(arr_out)

"""
This is a script implement merge sort
"""
import rand


def mergeSort(arr):
    """
    Merge Sort Function
    """
    if (len(arr) == 1):
        return arr

    half = len(arr) // 2

    return recombine(mergeSort(arr[:half]), mergeSort(arr[half:]))


def recombine(leftArr, rightArr):
    """
    recombine function, merge two sorted arrays
    """
    leftIndex = 0
    rightIndex = 0
    mergeArr = [None] * (len(leftArr) + len(rightArr))
    while leftIndex < len(leftArr) and rightIndex < len(rightArr):
        if leftArr[leftIndex] < rightArr[rightIndex]:
            mergeArr[leftIndex + rightIndex] = leftArr[leftIndex]
            leftIndex += 1
        else:
            mergeArr[leftIndex + rightIndex] = rightArr[rightIndex]
            rightIndex += 1
    
    while leftIndex < len(leftArr):
        mergeArr[leftIndex + rightIndex] = leftArr[leftIndex]
        leftIndex += 1
    while rightIndex < len(rightArr):
        mergeArr[leftIndex + rightIndex] = rightArr[rightIndex]
        rightIndex += 1
        
    return mergeArr


arr = rand.random_array([None] * 20)
arr_out = mergeSort(arr)

print(arr_out)

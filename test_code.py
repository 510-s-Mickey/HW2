"""
This is a test script for merge_sort function
"""
from hw2_debugging import merge_sort

def test_sorted_array():
    """
    Test if merge_sort correctly sorts an already sorted array
    """
    assert merge_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_unsorted_array():
    """
    Test if merge_sort correctly sorts an unsorted array
    """
    assert merge_sort([5, 3, 1, 4, 2]) == [1, 2, 3, 4, 5]

def test_array_with_duplicates():
    """
    Test if merge_sort correctly sorts an array with duplicate values
    """
    assert merge_sort([5, 3, 1, 4, 3]) == [1, 3, 3, 4, 5]

def test_array_with_negative_numbers():
    """
    Test if merge_sort correctly sorts an array with negative numbers
    """
    assert merge_sort([5, -3, 1, -7, 2]) == [-7, -3, 1, 2, 5]

def test_single_element_array():
    """
    Test if merge_sort correctly handles a single element array
    """
    assert merge_sort([1]) == [1]

def test_empty_array():
    """
    Test if merge_sort correctly handles an empty array
    """
    assert merge_sort([]) == []

def test_large_array():
    """
    Test if merge_sort correctly sorts a large array
    """
    large_array = list(range(1000, 0, -1))  # [1000, 999, ..., 1]
    sorted_array = list(range(1, 1001))     # [1, 2, ..., 1000]
    assert merge_sort(large_array) == sorted_array

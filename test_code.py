"""
This is a script test mergesort
"""
from hw2_debugging import merge_sort

def test_sorted1():
    """
    assert 
    """
    assert merge_Sort([5, 3, 1, 4, 2]) == [1, 2, 3, 4, 5]

def test_sorted2():
    """
    assrt
    """
    assert merge_sort([38, 27, 43, 3, 9, 82, 10]) == [3, 9, 10, 27, 38, 43, 82]

def test_sorted3():
    """
    assert
    """
    assert merge_sort([5, -3, 7, -3, 2, -1, 5]) == [-3, -3, -1, 2, 5, 5, 7]


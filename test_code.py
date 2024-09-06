from hw2_debugging import mergeSort
def test_sorted_array():
    assert mergeSort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_unsorted_array():
    assert mergeSort([5, 3, 1, 4, 2]) == [1, 2, 3, 4, 5]

# def test_empty_array():
#     assert mergeSort([]) == []

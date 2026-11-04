import Lab3

print("Test_Lab3")


def test_bubble_sort_ascending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_arr = [11, 12, 22, 25, 34, 64, 90]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert (result == test_arr)

def test_bubble_sort_descending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_arr = [90, 64, 34, 25, 22, 12, 11]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)

    assert (result == test_arr)

def test_bubble_sort_invalid():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]

    result = Lab3.bubble_sort(input_arr, 3)

    assert (result == [])

#EDITED PART AS PER EXERCISE 2

def test_bubble_sort_too_many():
    arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert Lab3.bubble_sort(arr, Lab3.SORT_ASCENDING) == 1

def test_bubble_sort_empty():
    arr = []
    assert Lab3.bubble_sort(arr, Lab3.SORT_ASCENDING) == 0

def test_bubble_sort_non_integer():
    arr = [5, 3, "meow", 1]
    assert Lab3.bubble_sort(arr, Lab3.SORT_ASCENDING) == 2
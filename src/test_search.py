from search import *


def test_binary_search_right():
    binary_search = binary_search_right
    nums = [1,3,4,4,4,9]
    assert binary_search(nums, 2) == -1
    assert binary_search(nums, 4) == 4
    nums = []
    assert binary_search(nums, 10) == -1
    nums = [0,1,1]
    assert binary_search(nums, 1) == 2
    assert binary_search(nums, 0) == 0
    nums = [3,3,5]
    assert binary_search(nums, 2) == -1
    assert binary_search(nums, 3) == 1
    assert binary_search(nums, 5) == 2
    assert binary_search(nums, 6) == -1


def test_binary_search_left():
    binary_search = binary_search_left
    nums = [1,3,4,4,4,9]
    assert binary_search(nums, 2) == -1
    assert binary_search(nums, 4) == 2
    nums = []
    assert binary_search(nums, 10) == -1
    nums = [0,1,1]
    assert binary_search(nums, 1) == 1
    assert binary_search(nums, 0) == 0
    nums = [3,3,5]
    assert binary_search(nums, 2) == -1
    assert binary_search(nums, 3) == 0
    assert binary_search(nums, 5) == 2
    assert binary_search(nums, 6) == -1


def test_binary_search():
    nums = [1,3,4,5,7,9]
    assert binary_search(nums, 2) == -1
    assert binary_search(nums, 4) == 2
    nums = []
    assert binary_search(nums, 10) == -1
    nums = [1]
    assert binary_search(nums, 1) == 0
    assert binary_search(nums, 0) == -1
    nums = [3,4,5]
    assert binary_search(nums, 2) == -1
    assert binary_search(nums, 3) == 0
    assert binary_search(nums, 5) == 2
    assert binary_search(nums, 6) == -1




def test_binary_search_insert_pos():
    binary_search = binary_search_insert_pos
    nums = [1,3,4,5,7,9]
    assert binary_search(nums, 2) == 1
    assert binary_search(nums, 4) == 2
    nums = []
    assert binary_search(nums, 10) == 0
    nums = [1]
    assert binary_search(nums, 1) == 0
    assert binary_search(nums, 0) == 0
    assert binary_search(nums, 2) == 1
    nums = [3,4,5]
    assert binary_search(nums, 2) == 0
    assert binary_search(nums, 3) == 0
    assert binary_search(nums, 5) == 2
    assert binary_search(nums, 6) == 3




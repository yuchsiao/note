
def binary_search(nums, target):
    if not nums: return -1
    left, right = 0, len(nums)-1
    while left <= right:  # assume at least one element
        mid = (left+right)//2
        if nums[mid] == target: return mid
        elif nums[mid] < target: left = mid+1
        else: right = mid-1
    return -1


def binary_search_insert_pos(nums, target):
    """leetcode tested"""
    if not nums: return 0
    left, right = 0, len(nums)-1
    while left <= right:  # assume at least one element
        mid = (left+right)//2
        if nums[mid] == target: return mid
        elif nums[mid] < target: left = mid+1
        else: right = mid-1
    return right+1


def binary_search_left(nums, target):
    """if duplicated keys, return the leftmost index i s.t. nums[i-1] < target <= nums[i]
    
    '0 n-1 < < 1 0 right'
    
    """
    if not nums: return -1 
    if len(nums) == 1: 
        if nums[0] == target: return 0
        else: return -1
    left, right = 0, len(nums)-1
    while left < right:
        mid = (left+right)//2
        if nums[mid] < target: left = mid+1
        else: right = mid
    if nums[right] != target:
        return -1
    else:
        return right


def binary_search_right(nums, target):
    """if duplicated keys, return the rightmost index i s.t. nums[i] <= target < nums[i+1]i
    
    '0 n < <= 1 0 left-1'

    """
    if not nums: return -1 
    if len(nums) == 1: 
        if nums[0] == target: return 0
        else: return -1
    left, right = 0, len(nums)
    while left < right:
        mid = (left+right)//2
        if nums[mid] <= target: left = mid+1
        else: right = mid
    if nums[left-1] != target:
        return -1
    else:
        return left-1





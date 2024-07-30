def twoNumberSum(array, targetSum):
    # Write your code here.
    array.sort()
    left = 0
    right = len(array)-1
    while left < right:
        if array[left] + array[right] == targetSum:
            return [array[left], array[right]]
        elif array[left] + array[right] < targetSum:
            left += 1
        elif array[left] + array[right] > targetSum:
            right -= 1
    return []
    pass

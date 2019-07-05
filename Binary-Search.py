data = [2, 4, 5, 7, 8, 9, 12, 14, 17, 19, 22, 25, 27, 28, 33, 37]
target = 28


# Linear Search
def linear_search(data, target):
    for i in range(len(data)):
        if data[i] == target:
            return i
    return False


# Iterative Binary Search
def binary_search_iterative(data, target):
    low = 0
    high = len(data) - 1

    while low <= high:
        mid = (low + high) // 2
        if target == data[mid]:
            return mid
        elif target < data[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return 'not found'


# Recursive Binart Search
def binary_seach_recursive(data, target, low, high):
    if low > high:
        return 'not found'
    else:
        mid = (low + high) // 2
        if target == data[mid]:
            return mid
        elif target < data[mid]:
            return binary_seach_recursive(data, target, low, mid - 1)
        else:
            return binary_seach_recursive(data, target, mid + 1, high)


print(binary_search_iterative(data, target))
print(binary_seach_recursive(data, target, 0, len(data) - 1))

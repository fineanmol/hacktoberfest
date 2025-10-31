def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid  # Found → return index
        elif arr[mid] < target:
            low = mid + 1  # Move right
        else:
            high = mid - 1  # Move left

    return -1  # Not found

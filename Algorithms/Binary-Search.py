def BinarySearch(arr, target):
    """
    Perform binary search on a sorted array to find the index of the target value.

    Parameters:
    arr (list): A list of sorted elements.
    target: The element to search for in the array.

    Returns:
    int: The index of the target element if found, otherwise -1.
    """
    i, j = 0, len(arr) - 1

    while i <= j:
        mid = i + (j - i) // 2

        # Check if target is present at mid
        if arr[mid] == target:
            return mid
        # If target is greater, ignore left half
        elif arr[mid] < target:
            i = mid + 1
        # If target is smaller, ignore right half
        else:
            j = mid - 1

    # Target was not found in the array
    return -1

# Example usage:
result = BinarySearch([1, 2, 3, 4, 5, 6, 7, 8, 9], 5)
print("Element found at index:", result)

'''
Remarks:
- All idea behind this this logic is Divider Array in two parts then compare the middle element with target value.
Floor division (//) has higher precedence than addition (+).
'''
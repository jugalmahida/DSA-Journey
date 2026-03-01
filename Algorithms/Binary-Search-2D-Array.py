def BinarySearchIn2DArray(arr, target):
    totalColumns = len(arr[0])
    totalRows = len(arr)
    i , j = 0, totalColumns * totalRows - 1;
    while j <= i:
        mid =  i + (j - i) // 2
        rowIndex = mid // 2
        columnIndex = mid % 2

        if arr[rowIndex,columnIndex] == target:
            return [rowIndex,columnIndex]
        elif arr[rowIndex,columnIndex] < target:
            i = mid + 1
        else:
            j = mid - 1
    return -1

# Example usage:
result = BinarySearchIn2DArray([ [1, 2, 3], 
                                [4, 5, 6], 
                                [7, 8, 9], 
                                [9, 11, 15] ], 7)
print("Element found at index:", result)

'''
Remarks:
- Main things this we can assume this 2d array in a 1D virtual array & important thing is
converting 1D array's index into 2D array indices like we got 6 index, in real 2D array it should be [2,0], we can achieve this with following formula
rowIndex = currentIndex // totalColumns
columnIndex = currentIndex % totalColumns
totalNumber = totalColumns x totalRows
'''
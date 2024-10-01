def binary_search_matrix(matrix, target):
    if not matrix or not matrix[0]:
        return None

    rows = len(matrix)
    cols = len(matrix[0])
    low, high = 0, rows * cols - 1

    while low <= high:
        mid = (low + high) // 2
        mid_value = matrix[mid // cols][mid % cols]  # Convert 1D index to 2D indices

        if mid_value == target:
            return (mid // cols, mid % cols)  # Return the 2D index

        if mid_value < target:
            low = mid + 1
        else:
            high = mid - 1

    return None


# Example usage:
matrix = [
    [1, 3, 5, 8],
    [7, 10, 11, 15],
    [12, 14, 16, 28]
]
target = 1
index = binary_search_matrix(matrix, target)

if index:
    print(f"Number {target} found at index: {index}")
else:
    print(f"Number {target} not found in the matrix.")


def swap(x, y):
    """
    Task 1:
    - Swap the values of x and y using only x and y as variables.
    - x and y must be numeric.
    - Return -1 if x and y are not numeric.
    """
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        return -1
    x, y = y, x
    print("Swapped values:", x, y)
    return x, y

# Test cases
print("Result 1:", swap("Apple", 10))   # Should return -1
print("Result 2:", swap(9, 17))         # Should print: Swapped values: 17 9

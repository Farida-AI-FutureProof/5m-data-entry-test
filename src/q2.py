# Task 2: Run test cases
print("Result 1:", swap("Apple", 10))   # Should return -1
print("Result 2:", swap(9, 17))         # Should print: Swapped values: 17 9

def find_and_replace(lst, find_val, replace_val):
    """
    Task 1
    - Create a function that searches for all occurrences of a value (find_val) in a given list (lst)
      and replaces them with another value (replace_val).
    - lst must be a list.
    - Return the modified list.
    """
    if not isinstance(lst, list):
        return "Invalid input"

    result = [replace_val if item == find_val else item for item in lst]
    return result


# Task 2: Run test cases
print("Test 1:", find_and_replace([1, 2, 3, 4, 2, 2], 2, 5))
print("Test 2:", find_and_replace(["apple", "banana", "apple"], "apple", "orange"))

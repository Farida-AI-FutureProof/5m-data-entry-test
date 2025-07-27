def find_first_negative(lst):
    """
    Task 6:
    - Create a function that finds the first negative number in a list (lst).
    - Return the first negative number if found, otherwise return "No negatives".
    - Use a while loop to implement this.
    """
    if not isinstance(lst, list):
        return "Invalid input"

    i = 0
    while i < len(lst):
        if isinstance(lst[i], (int, float)) and lst[i] < 0:
            return lst[i]
        i += 1
    return "No negatives"

# Test cases
print("Test 1:", find_first_negative([3, 5, -1, 7, -2, 8]))  # Should return -1
print("Test 2:", find_first_negative([2, 10, 7, 0]))         # Should return "No negatives"
print("Test 3:", find_first_negative("not a list"))          # Should return "Invalid input"

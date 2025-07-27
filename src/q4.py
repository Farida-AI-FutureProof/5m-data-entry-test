def string_reverse(s):
    """
    Task 4:
    - Create a function that reverses a given string (s).
    - s must be a string.
    - Return the reversed string.
    """
    if not isinstance(s, str):
        return "Invalid input"
    
    return s[::-1]

# Test cases
print("Test 1:", string_reverse("Hello World"))  # "dlroW olleH"
print("Test 2:", string_reverse("Python"))       # "nohtyP"
print("Test 3:", string_reverse(12345))          # "Invalid input"

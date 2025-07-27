def check_divisibility(num, divisor):
    """
    Task 5:
    - Create a function to check if the number (num) is divisible by another number (divisor).
    - Both num and divisor must be numeric.
    - Return True if num is divisible by divisor, False otherwise.
    """
    if not isinstance(num, (int, float)) or not isinstance(divisor, (int, float)):
        return "Invalid input"
    if divisor == 0:
        return "Division by zero is not allowed"

    return num % divisor == 0

# Test cases
print("Test 1:", check_divisibility(10, 2))   # True
print("Test 2:", check_divisibility(7, 3))    # False
print("Test 3:", check_divisibility("10", 2)) # "Invalid input"
print("Test 4:", check_divisibility(10, 0))   # "Division by zero is not allowed"

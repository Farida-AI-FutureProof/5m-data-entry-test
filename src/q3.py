def update_dictionary(dct, key, value):
    """
    Task 3:
    - Create a function that updates a dictionary (dct) with a new key-value pair.
    - If the key already exists in dct, print the original value, then update its value.
    - Return the updated dictionary.
    """
    if not isinstance(dct, dict):
        return "Invalid input"
    
    if key in dct:
        print("Original value:", dct[key])
    
    dct[key] = value
    return dct

# Test cases
print("Test 1:", update_dictionary({}, "name", "Alice"))
print("Test 2:", update_dictionary({"age": 25}, "age", 26))

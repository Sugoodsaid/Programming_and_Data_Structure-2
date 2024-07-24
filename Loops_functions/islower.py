def islower(c):
    if ord('a') <= ord(c) <= ord('z'):
        return True
    else:
        return False

# Test the function
print(islower('a'))  # True
print(islower('A'))  # False
print(islower('z'))  # True
print(islower('Z'))  # False

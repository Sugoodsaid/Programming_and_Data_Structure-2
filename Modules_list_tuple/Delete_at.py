def delete_at(my_list, idx):
    # Check if the index is out of bounds
    if idx < 0 or idx >= len(my_list):
        return my_list
    
    # Create a new list excluding the item at the specified index
    new_list = my_list[:idx] + my_list[idx+1:]
    return new_list

# Example usage
my_list = [1, 2, 3, 4, 5]
idx = 3
new_list = delete_at(my_list, idx)

print(new_list)  # Output: [1, 2, 3, 5]
print(my_list)   # Output: [1, 2, 3, 4, 5]

 search_replace(my_list, search, replace):
  
    new_list = []
    
    for element in my_list:
    
        if element == search:
            new_list.append(replace)
        else:
            new_list.append(element)
    
    return new_list

# Example usage
my_list = [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
new_list = search_replace(my_list, 2, 89)
print(new_list)  # Output: [1, 89, 3, 4, 5, 4, 89, 1, 1, 4, 89]
print(my_list)  # Output: [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]

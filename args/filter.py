
def filter_and_modify(data_list, **kwargs):
    filtered_and_modified = []
    
    for item in data_list:
        if all(item.get(key) == value for key, value in kwargs.items() if key in item):
            modified_item = item.copy()
            for key, value in kwargs.items():
                modified_item[key] = value
            filtered_and_modified.append(modified_item)
    
    return filtered_and_modified

# Example usage
data = [
    {"name": "Alice", "age": 30, "city": "New York"},
    {"name": "Bob", "age": 25, "city": "Los Angeles"},
    {"name": "Charlie", "age": 35, "city": "New York"},
    {"name": "Diana", "age": 30, "city": "Chicago"}
]

filtered_data = filter_and_modify(data, age=30, city="New York", occupation='Engineer')
print(filtered_data)  
# Output: [{'name': 'Alice', 'age': 30, 'city': 'New York', 'occupation': 'Engineer'}]

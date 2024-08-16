def sum_args(*args):
    # Initialize the sum to 0
    total = 0
    for num in args:
        # Add the argument to the total sum
        total += num
    return total

# Example usage
print(sum_args(1, 2, 3))          # Output: 6
print(sum_args(10, 20, 30, 40))  # Output: 100
print(sum_args())                # Output: 0
print(sum_args(5.5, 4.5, -10))   # Output: 0

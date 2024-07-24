# Print numbers from 00 to 99 separated by ", " with a newline at the end

# Use one loop and no more than 2 print functions with string format
for num in range(100):
    print(f"{num:02}", end=', ' if num < 99 else '\n')

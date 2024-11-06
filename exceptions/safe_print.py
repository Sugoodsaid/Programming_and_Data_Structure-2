def sum_arguments(*args):
    total = 0
    for arg in args:
        total += arg
    return total

def safe_print_list(my_list=[], x=0):
    printed_count = 0
    for i in range(x):
        try:
            print(my_list[i], end=' ')
            printed_count += 1
        except IndexError:
            break
    print()  # for new line
    return printed_count

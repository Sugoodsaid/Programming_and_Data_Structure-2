for i in range(ord('z'), ord('A') - 1, -1):
    print(chr(i) + chr(i - 32) if i % 2 == 1 else chr(i), end='')

print()

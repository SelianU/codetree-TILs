def print_star(n):
    if n == 0:
        return

    print_star(n-1)
    print("HelloWorld")

print_star(4)
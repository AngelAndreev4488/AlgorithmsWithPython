def print_figure(n):
    if n == 0:
        return
    print("*" * n)
    print_figure(n - 1)
    print("#" * n)


number = int(input())
print_figure(number)

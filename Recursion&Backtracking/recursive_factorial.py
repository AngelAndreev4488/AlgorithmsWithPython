def factorial_calc(num, idx):
    if idx == num:
        return num
    return idx * factorial_calc(num, idx + 1)


number = int(input())
print(factorial_calc(number, 1))

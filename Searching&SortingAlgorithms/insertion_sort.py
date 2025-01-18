numbers = [int(x) for x in input().split()]
arr_len = len(numbers)

for i in range(arr_len):
    j = i
    while j > 0 and numbers[j] < numbers[j - 1]:
        numbers[j - 1], numbers[j] = numbers[j], numbers[j - 1]
        j -= 1

print(*numbers)

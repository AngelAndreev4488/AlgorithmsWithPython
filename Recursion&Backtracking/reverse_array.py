def reverse(numbers, index):
    if index == len(numbers) // 2:
        return

    swap_index = len(numbers) - 1 - index
    numbers[index], numbers[swap_index] = numbers[swap_index], numbers[index]
    reverse(numbers, index + 1)


numbers = input().split()

reverse(numbers, 0)

print(' '.join(numbers))


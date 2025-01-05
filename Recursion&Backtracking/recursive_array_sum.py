def show_sum(numbers, idx):
    if idx == len(numbers) - 1:
        return numbers[idx]
    return numbers[idx] + show_sum(numbers, idx + 1)


array = [int(x) for x in input().split()]

print(show_sum(array, 0))


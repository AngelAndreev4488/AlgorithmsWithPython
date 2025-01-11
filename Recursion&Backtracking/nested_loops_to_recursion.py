def nested_arr(idx, array):
    if idx >= len(array):
        print(*array, sep=' ')
        return
    for num in range(1, len(array) + 1):
        array[idx] = num
        nested_arr(idx + 1, array)


n = int(input())
arr = [None] * n

nested_arr(0, arr)

def selection_sort(array, size):
    for ind in range(size):
        min_index = ind

        for j in range(ind + 1, size):

            if array[j] < array[min_index]:
                min_index = j

        (array[ind], array[min_index]) = (array[min_index], array[ind])


arr = [int(x) for x in input().split()]
size = len(arr)
selection_sort(arr, size)

print(*arr)

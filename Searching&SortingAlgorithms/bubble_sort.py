def bubble_sort(array):
    n = len(array)
    for i in range(n):

        swapped = False

        for j in range(0, n - i - 1):

            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True

        if not swapped:
            break


numbers = [int(x) for x in input().split()]
bubble_sort(numbers)
print(*numbers)

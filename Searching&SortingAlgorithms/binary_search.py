def binary_search(array, number):
    left_index = 0
    right_index = len(array) - 1

    while left_index <= right_index:
        mid_idx = (left_index + right_index) // 2
        mid_num = array[mid_idx]

        if mid_num == number:
            return mid_idx

        if number > mid_num:
            left_index = mid_idx + 1
        else:
            right_index = mid_idx - 1
    return -1


numbers = [int(x) for x in input().split()]
searched_number = int(input())

print(binary_search(numbers, searched_number))

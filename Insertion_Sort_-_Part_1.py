"""
Insertion Sort - Part 1
"""

def insertionSort1(n, arr):

    candidate = arr[-1]
    last_swap_element = None

    for i in range(n-1, -1, -1):
        if arr[i] > candidate:
            arr[i + 1] = arr[i]
            last_swap_element = i

            for i in range(n):
                print(arr[i], end=" ")
            print()
        else:
            break

    if last_swap_element:
        arr[last_swap_element] = candidate
    else:
        arr[0] = candidate

    for i in range(n):
        print(arr[i], end=" ")
    print()


n = 10
my_lsit = [2, 3, 4, 5, 6, 7, 8, 9, 10, 1]


insertionSort1(n, my_lsit)

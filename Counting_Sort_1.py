
def countingSort(arr):
    counting_array = [0] * 100

    for num in arr:
        counting_array[num] += 1
    
    return counting_array



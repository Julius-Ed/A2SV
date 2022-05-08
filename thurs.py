
# Time: O(nlogn)
# Space: O(1)
def carParkingRoof(cars, k):
    cars.sort()

    # use a sliding window with size k.
    res = cars[k - 1] - cars[0] + 1

    # the distance between the leftmost and rightmost car in the window
    # is given by the value at index right - index left + 1.

    for right in range(k - 1, len(cars)):
        # move window through array and find the one with smallest distance.
        res = min(cars[right] - cars[right - k + 1] + 1, res)

    return res


print(carParkingRoof([6, 2, 12, 7], 3))  # 6
print(carParkingRoof([2, 10, 8, 17], 3))  # 9
print(carParkingRoof([1, 2, 3, 10], 4))


print(carParkingRoof([6, 2, 12, 7], 1))  # 1

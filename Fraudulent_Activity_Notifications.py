from collections import deque

def activityNotifications(expenditure, d):

    result = 0
    countingSortArray = [0] * (max(expenditure) + 1)

    trace = deque(expenditure[:d])

    for value in trace:
        countingSortArray[value] += 1

    for expenditureIndex in range(d, len(expenditure)):
        median = getMedian(countingSortArray, d)

        if expenditure[expenditureIndex] >= 2 * median:
            result += 1

        countingSortArray[trace.popleft()] -= 1
        trace.append(expenditure[expenditureIndex])

        countingSortArray[expenditure[expenditureIndex]] += 1

    return result

def getMedian(countingSortArray, d):

    if d % 2 == 0:
        median = (getNthValue(countingSortArray, (d // 2) + 1) +
                  getNthValue(countingSortArray, (d // 2))) / 2

    else:
        median = getNthValue(countingSortArray, ((d + 1) // 2))

    return median

def getNthValue(countingSortArray, threshold):

    cursor, counter = -1, 0

    while counter < threshold and cursor < len(countingSortArray):
        cursor += 1
        counter += countingSortArray[cursor]

    return cursor
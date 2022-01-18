

def domino_piling(m, n):

    if m < 1 or n < 1:
        return 0

    if m % 2 == 0 or n % 2 == 0:
        return int(m * n / 2)

    greater_element = max(m, n)
    smaller_element = min(m, n)

    stones = ((greater_element - 1) * smaller_element) / 2
    stones += (smaller_element - 1) / 2

    return int(stones)


#m, n = list(map(int, input().split()))
#print(domino_piling(m, n))

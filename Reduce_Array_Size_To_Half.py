"""
You are given an integer array arr. You can choose a set of integers and remove all the occurrences of 
these integers in the array.

Return the minimum size of the set so that at least half of the integers of the array are removed.
"""


from collections import Counter
import heapq


class Solution:
    def minSetSizeBF(self, arr) -> int:

        counting_dict = Counter(arr)

        total = sum(counting_dict.values())

        counter = 0

        while total > len(arr) // 2:
            max_key = None
            max_ocurrences = 0

            for number in counting_dict:

                if counting_dict[number] > max_ocurrences:
                    max_key = number
                    max_ocurrences = counting_dict[number]

            counter += 1

            total -= counting_dict[max_key]

            counting_dict[max_key] = 0

        return counter

    def minSetSize(self, arr) -> int:

        counting_dict = Counter(arr)

        total = 0
        my_heap = []

        for num in counting_dict:

            occurences = counting_dict[num]
            total += occurences

            heapq.heappush(my_heap, occurences * (-1))

        i = 0

        while total > len(arr) // 2:

            i += 1

            max_occurences = heapq.heappop(my_heap)

            total -= max_occurences * (-1)

        return i


# arr = [3,3,3,3,5,5,5,2,2,7] # -> 2
arr = [7, 7, 7, 7, 7, 7]  # -> 1


Sol = Solution()

print(Sol.minSetSize(arr))

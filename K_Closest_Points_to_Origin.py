import imp
import math
import heapq


class Solution:
    def kClosest(self, points, k):

        results = []
        distance_dictionary = {}

        for point in points:
        
            distance = math.sqrt((point[0]**2) + (point[1] ** 2))
            if distance not in distance_dictionary:
                distance_dictionary[distance] = [point]
            else:
                distance_dictionary[distance] += [point]

        my_heap = []

        for key in distance_dictionary:
            if len(distance_dictionary[key]) > 1:
                heapq.heappush(my_heap, key)
                heapq.heappush(my_heap, key)
            else:
                heapq.heappush(my_heap, key)

        while len(results) < k:

            values = distance_dictionary[heapq.heappop(my_heap)]

            for value in values:
                results.append(value)

        return results


Sol = Solution()
print(Sol.kClosest([[0, 1], [1, 0]], 2))

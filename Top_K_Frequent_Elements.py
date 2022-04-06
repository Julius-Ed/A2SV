from typing import List
from collections import Counter
import heapq


# O(k * log(n))

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # O(n)
        numToCount = Counter(nums)
        maxHeap = []

        # O(n)
        for num in numToCount:
            maxHeap.append([numToCount[num] * (- 1), num])

        # O(n)
        heapq.heapify(maxHeap)

        res = []

        #O(k * log(n))
        while len(res) < k:
            res.append(heapq.heappop(maxHeap)[1])

        return res


Sol = Solution()
print(Sol.topKFrequent([1, 1, 1, 2, 2, 3], 2))
print(Sol.topKFrequent([1, 2], 2))

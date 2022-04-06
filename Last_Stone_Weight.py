import heapq
from typing import List
import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        for index, stone in enumerate(stones):
            stones[index] = stone * (-1)

        heapq.heapify(stones)

        while len(stones) > 1:
            y = heapq.heappop(stones) * (-1)
            x = heapq.heappop(stones) * (-1)

            if x < y:
                heapq.heappush(stones, (y-x) * (-1))

        if len(stones) > 0:
            return stones[0] * (-1)

        return 0


Sol = Solution()
print(Sol.lastStoneWeight([2, 7, 4, 1, 8, 1]))

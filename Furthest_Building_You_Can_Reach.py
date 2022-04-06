from typing import List
import heapq


class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:

        usedBricks = []

        for index in range(1, len(heights)):

            slope = heights[index] - heights[index - 1]

            # if we stay at same level or go down we don't need bricks nor ladders
            if slope <= 0:
                continue

            # use bricks if possible.
            if slope <= bricks:
                heapq.heappush(usedBricks, slope * (-1))
                bricks -= slope

            elif ladders > 0 and len(usedBricks) > 0 and usedBricks[0] * (-1) > slope:

                # replace biggest past climb with ladder.
                ladders -= 1
                bricks += heapq.heappop(usedBricks) * (-1)

                # make new climb with bricks.
                heapq.heappush(usedBricks, slope * (-1))
                bricks -= slope

            elif ladders > 0:
                ladders -= 1

            else:
                return index - 1

        return len(heights) - 1


Sol = Solution()
print(Sol.furthestBuilding([4, 2, 7, 6, 9, 14, 12], 5, 1))
print(Sol.furthestBuilding([2, 7, 9, 12], 5, 1))  # expected = 3

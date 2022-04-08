from typing import List
from collections import deque


class Solution:
    # Time complexity: O(N)
    # Space complexity: O(1)

    def canReach(self, arr: List[int], start: int) -> bool:

        q = deque([start])

        while q:

            current = q.popleft()

            childLeft, childRight = current + \
                arr[current], current - arr[current]

            print(arr)
            # mark visited indices by turning their corresponding values to -1.
            arr[current] = -1

            # check for out of bound error. Only add nodes to the queue that have not been visited yet.
            if 0 <= childLeft < len(arr) and arr[childLeft] != -1:
                q.append(childLeft)

            if 0 <= childRight < len(arr) and arr[childRight] != -1:
                q.append(childRight)

        # loop through array and check if any zeros have not been visited.
        for num in arr:
            if num == 0:
                return False

        return True


Sol = Solution()
# print(Sol.canReach([4, 2, 3, 0, 3, 1, 2], 5))
# print(Sol.canReach([4, 2, 3, 0, 3, 1, 2], 0))
# print(Sol.canReach([3, 0, 2, 1, 2], 2))
# print(Sol.canReach([5], 0))
# print(Sol.canReach([0, 0], 0))


print(Sol.canReach([0, 3, 0, 6, 3, 3, 4], 6))  # expected: true

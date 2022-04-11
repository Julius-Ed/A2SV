from typing import List
import heapq


class Solution:
    # think of the problem as a graph problem, where rows and cols are monotonically increasing
    # and use a heap instead of a queue.
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:

        res, visited = [], set()

        q = [(nums1[0] + nums2[0], 0, 0)]

        while q and len(res) < k:

            sum, row, col = heapq.heappop(q)
            res.append((nums1[row], nums2[col]))

            if 0 <= row + 1 < len(nums1) and (row + 1, col) not in visited:
                visited.add((row + 1, col))
                heapq.heappush(q, (nums1[row + 1] + nums2[col], row + 1, col))

            if 0 <= col + 1 < len(nums2) and (row, col + 1) not in visited:
                visited.add((row, col + 1))
                heapq.heappush(q, (nums1[row] + nums2[col + 1], row, col + 1))

        return res


Sol = Solution()
print(Sol.kSmallestPairs([1, 1, 2], [1, 2, 3], 9))

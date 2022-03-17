from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:

        left, right = 0, len(citations) - 1

        # left is n. on the right hand side of mid everything must be greater than h.
        # at position i, there are len(citations) - i - 1 papers with citations > citations[i]
        # the constraint that the other i papers have fewer citations is fulfilled since the list is sorted.

        while left <= right:

            mid = (left + right) // 2

            if citations[mid] == len(citations) - mid:
                return len(citations) - mid

            if citations[mid] < len(citations) - mid:
                left = mid + 1

            else:
                right = mid - 1

        return len(citations) - left


Sol = Solution()
print(Sol.hIndex([0, 1, 3, 5, 6]))

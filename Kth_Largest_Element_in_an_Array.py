from typing import List
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        for i, num in enumerate(nums):
            nums[i] = num * (-1)

        heapq.heapify(nums)

        counter = 0
        res = nums[0] * (-1)

        while counter < k:
            res = heapq.heappop(nums) * (-1)
            counter += 1

        return res


Sol = Solution()
print(Sol.findKthLargest([3, 2, 1, 5, 6, 4], k=2))

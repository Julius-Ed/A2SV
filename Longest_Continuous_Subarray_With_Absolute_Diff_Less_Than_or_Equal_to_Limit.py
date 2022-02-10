from typing import List
import heapq


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:

        longestSubarray = 1
        currentSubarrayLength = 1

        minHeap = heapq.heapify([nums[0]])
        maxHeap = heapq.heapify((-1)*[nums[0]])

        left = right = 0

        while right < len(nums):
            
            maxVal = heapq.heappop(maxHeap)# * (-1)
            minVal = heapq.heappop(minHeap)

            heapq.heappush(minHeap, nums[right])
            heapq.heappush(maxHeap, (-1) * nums[right])

            print(maxVal, minVal)

            right += 1


Sol = Solution()
print(Sol.longestSubarray([8, 2, 4, 7], 4) == 2)
print(Sol.longestSubarray([10, 1, 2, 4, 7, 2], 5) == 4)
print(Sol.longestSubarray([8], 10) == 1)

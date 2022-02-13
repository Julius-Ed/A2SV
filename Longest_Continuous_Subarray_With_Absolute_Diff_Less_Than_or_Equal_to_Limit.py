from typing import List
from collections import deque


class Solution:

    def longestSubarray(self, nums: List[int], limit: int) -> int:

        minDequeue = deque()
        maxDequeue = deque()

        leftIndex = 0
        rightIndex = 0

        longestSubstringCounter = 0

        while rightIndex < len(nums):

            while minDequeue and nums[rightIndex] <= nums[minDequeue[-1]]:
                minDequeue.pop()

            while maxDequeue and nums[rightIndex] >= nums[maxDequeue[-1]]:
                maxDequeue.pop()

            minDequeue.append(rightIndex)
            maxDequeue.append(rightIndex)

            while nums[maxDequeue[0]] - nums[minDequeue[0]] > limit:

                leftIndex += 1
                if leftIndex > minDequeue[0]:
                    minDequeue.popleft()
                if leftIndex > maxDequeue[0]:
                    maxDequeue.popleft()

            longestSubstringCounter = max(
                longestSubstringCounter, rightIndex - leftIndex + 1)
            rightIndex += 1

        return longestSubstringCounter


Sol = Solution()

print(Sol.longestSubarray([8, 2, 4, 7], 4) == 2)
print(Sol.longestSubarray([10, 1, 2, 4, 7, 2], 5) == 4)
print(Sol.longestSubarray([8], 10) == 1)

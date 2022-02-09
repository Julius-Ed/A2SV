from typing import List


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:

        longestSubarray = 1
        currentSubarrayLength = 1

        minValueSubarray = nums[0]
        maxValueSubarray = nums[0]

        left = 0
        right = 1

        while right < len(nums):

            minValueSubarray = min(nums[right], minValueSubarray)
            maxValueSubarray = max(nums[right], maxValueSubarray)

            if abs(nums[right] - minValueSubarray) > limit or abs(nums[right] - maxValueSubarray) > limit:
                left += 1
                right = left + 1
                currentSubarrayLength = 1
                if right < len(nums):
                    minValueSubarray = min(nums[left], nums[right])
                    maxValueSubarray = max(nums[left], nums[right])

            else:
                currentSubarrayLength += 1
                right += 1

            if currentSubarrayLength > longestSubarray:
                longestSubarray = currentSubarrayLength

        return longestSubarray

        def validRange(self, left, right, minValue, maxValue):
            pass


Sol = Solution()
print(Sol.longestSubarray([8, 2, 4, 7], 4) == 2)
print(Sol.longestSubarray([10,1,2,4,7,2], 5) == 4)
print(Sol.longestSubarray([8], 10) == 1)

from typing import List

# O(n*log(n))


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        # the duplicate value must be in this range.
        lowTarget, highTarget = 0, len(nums) - 1

        # O(log(n))
        while lowTarget <= highTarget:

            mid = (lowTarget + highTarget) // 2

            # O(n)
            if self.duplicate(nums, mid):
                dup = mid
                highTarget = mid - 1
            else:
                lowTarget = mid + 1

        return dup

    def duplicate(self, nums, target):
        # the lowest number for which numbers with a face value lower or equal to target exist in nums, is a duplicate.
        count = 0

        for num in nums:
            if num <= target:
                count += 1

        if count > target:
            return True

        return False


Sol = Solution()

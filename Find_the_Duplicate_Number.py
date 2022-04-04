from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        lowTarget, highTarget = 0, len(nums) - 1

        while lowTarget <= highTarget:

            mid = (lowTarget + highTarget) // 2

            if self.duplicate(nums, mid):
                dup = mid
                highTarget = mid - 1
            else:
                lowTarget = mid + 1

        return dup

    def duplicate(self, nums, target):

        count = 0

        for num in nums:
            if num <= target:
                count += 1

        if count > target:
            return True

        return False


Sol = Solution()

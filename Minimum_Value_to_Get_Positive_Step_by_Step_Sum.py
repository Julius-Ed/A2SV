from typing import List


class Solution:
    def minStartValue(self, nums: List[int]) -> int:

        acc = nums[0]
        for numIndex in range(1, len(nums)):
            acc += nums[numIndex]
            nums[numIndex] = acc

        k = (min(nums) * -1) + 1

        return max(k, 1)


Sol = Solution()

print(Sol.minStartValue([-3, 2, -3, 4, 2]) == 5)
print(Sol.minStartValue([1, 2]) == 1)
print(Sol.minStartValue([1, -2, -3]) == 5)

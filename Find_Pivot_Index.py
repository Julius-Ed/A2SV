from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        rightHandSideSum = sum(nums)
        leftHandSideSum = 0

        for index, value in enumerate(nums):
            rightHandSideSum -= value

            if rightHandSideSum == leftHandSideSum:
                return index

            leftHandSideSum += value

        return - 1


Sol = Solution()

print(Sol.pivotIndex([1, 7, 3, 6, 5, 6]) == 3)
print(Sol.pivotIndex([1,2,3]) == - 1)
print(Sol.pivotIndex([2, 1, -1]))

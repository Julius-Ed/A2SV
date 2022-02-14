from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:

        acc = nums[0]
        for numIndex in range(1, len(nums)):
            acc += nums[numIndex]
            nums[numIndex] = acc

        return nums

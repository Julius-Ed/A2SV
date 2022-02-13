from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        preSum = nums[0]
        maxSum = nums[0]
        allNegatives = True

        for numIndex in range(1, len(nums)):
            if nums[numIndex] > 0:
                allNegatives = False

            if preSum < 0:
                preSum = nums[numIndex]
            else:
                preSum += nums[numIndex]

            if preSum > maxSum:
                maxSum = preSum

        if allNegatives:
            return maxSum

        preSum = nums[0]
        minSum = nums[0]

        for numIndex in range(1, len(nums)):
            if preSum > 0:
                preSum = nums[numIndex]
            else:
                preSum += nums[numIndex]

            if preSum < minSum:
                minSum = preSum

        maxSumIfWarpped = sum(nums) - minSum

        return max(maxSumIfWarpped, maxSum)


Sol = Solution()
print(Sol.maxSubarraySumCircular([5, -3, 5]) == 10)
print(Sol.maxSubarraySumCircular([1, -2, 3, -2]) == 3)
print(Sol.maxSubarraySumCircular([-3, -2, -3]) == -2)
print(Sol.maxSubarraySumCircular([1, -2, 2, 1]) == 4)
print(Sol.maxSubarraySumCircular([-4]) == -4)
print(Sol.maxSubarraySumCircular([1, -6, -7, 4]) == 5)
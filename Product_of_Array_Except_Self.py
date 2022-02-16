from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        forwardAccProd = [1] * (len(nums))
        forwardAcc = 1
        backwardAccProd = [1] * (len(nums))
        backwardAcc = 1

        result = [0] * len(nums)

        for numIndex, num in enumerate(nums):
            forwardAcc *= num
            forwardAccProd[numIndex] = forwardAcc

        for numIndex in range(len(nums) - 1, -1, -1):
            num = nums[numIndex]
            backwardAcc *= num
            backwardAccProd[numIndex] = backwardAcc

        forwardAccProd = [1] + forwardAccProd + [1]
        backwardAccProd = [1] + backwardAccProd + [1]

        for index in range(len(result)):
            result[index] = forwardAccProd[index] * backwardAccProd[index + 2]

        return result


Sol = Solution()
print(Sol.productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6])
print(Sol.productExceptSelf([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0])

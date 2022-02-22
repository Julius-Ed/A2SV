from typing import List


class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:

        acc = 0
        for index, num in enumerate(nums):
            acc += num
            nums[index] = acc
        nums.insert(0, 0)

        result = LMax = MMax = 0

        for index in range(firstLen+secondLen, len(nums)):
        
            LSum = nums[index-secondLen] - nums[index-secondLen-firstLen]
            MSum = nums[index] - nums[index-secondLen]
    
            LMax = max(LMax, LSum)
            result = max(result, LMax + MSum)

        for index in range(firstLen+secondLen, len(nums)):

            MSum = nums[index-firstLen] - nums[index-secondLen-firstLen]
            LSum = nums[index] - nums[index-firstLen]
    
            MMax = max(MMax, MSum)
            result = max(result, MMax + LSum)

        return result


Sol = Solution()
print(Sol.maxSumTwoNoOverlap([1, 4, 2, 10, 2, 3, 1, 0, 20], 3, 1))

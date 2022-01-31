
class Solution:
    def maxSubArray(self, nums) -> int:
        
        preSum = nums[0]
        maxSum = nums[0]

        for num_index in range(1, len(nums)):
            if preSum < 0:
                preSum = nums[num_index]
            else:
                preSum += nums[num_index]
    
            if preSum > maxSum:
                 maxSum = preSum
        
        return maxSum

Sol = Solution()

print(Sol.maxSubArray([-2, 1]))
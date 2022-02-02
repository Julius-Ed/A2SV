class Solution:
    def firstMissingPositive(self, nums) -> int:
        
        for index, num in enumerate(nums):
            
            if num < 0:
                nums[index] = 0
        
        for index, num in enumerate(nums):

            if abs(num) >= 1 and abs(num) <= len(nums) and nums[abs(num) - 1] == 0:
                nums[abs(num) - 1] = (len(nums) + 1) * (-1)
                continue

            if abs(num) >= 1 and abs(num) <= len(nums) and nums[abs(num) - 1] > 0:
                nums[abs(num) - 1] = nums[abs(num) - 1] * (-1)
            
        
        for candidate_solution in range(0, len(nums)):
            if nums[candidate_solution] >= 0:
                return candidate_solution + 1
        
        return len(nums) + 1
        


Sol = Solution()
print(Sol.firstMissingPositive([-1, 2]))
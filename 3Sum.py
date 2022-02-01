
class Solution:
    def threeSum(self, nums):

        res = set()
        
        nums.sort()

        for index, num in enumerate(nums):

            
            target_sum = -num

            left = index + 1
            right = len(nums) - 1

            while left < right:
                
                if nums[left] + nums[right] == target_sum:
                    result = [nums[left], nums[right], num]
                    result.sort()
                    result = tuple(result)

                    if result not in res:
                        res.add(result)

                
                if nums[left] + nums[right] < target_sum:
                    left += 1
                
                else:
                    right -= 1


        return list(res)


Sol = Solution()

nums = [-1, 0, 1, 2, -1, -4] # -> [[-1,-1,2],[-1,0,1]]
#nums = [0, 0, 0, 0]
#nums = []
#nums = [1,2,-2,-1]

print(Sol.threeSum(nums))
class Solution:
    def searchRange(self, nums, target: int):
        
        low = 0
        high = len(nums) - 1

        while low <= high:

            mid = (high + low) // 2

            if mid > len(nums) - 1:
    
                return len(nums)
        
            if mid < 0:
                return -1


            if nums[mid] < target:
                low = mid + 1

            elif nums[mid] > target:
                high = mid - 1

            else:
                
                go_left = mid
                go_right = mid

                while go_left > 0 and nums[go_left] == nums[go_left - 1]:
                    go_left -= 1
                
                while go_right < len(nums) - 1 and nums[go_right] == nums[go_right + 1]:
                    go_right += 1
                
                return [go_left, go_right]

            


        return [-1, -1]

Sol = Solution()
print(Sol.searchRange([], 4))


"""
Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
"""
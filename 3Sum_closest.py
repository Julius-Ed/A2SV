
class Solution:
    def threeSumClosest(self, nums, target: int) -> int:
        
        nums.sort()

        best_fitting_sum = nums[0] + nums[1] + nums[2]
        distance_to_target = abs(target - best_fitting_sum)

        for i, num in enumerate(nums):
            sum_left_right = target - num

            left = i + 1
            right = len(nums) - 1

            while left < right:

                if nums[left] + nums[right] == sum_left_right:
                    return target
                
                current_distance_to_target = abs(nums[left] + nums[right] + num - target)

                if current_distance_to_target < distance_to_target:
                    best_fitting_sum = nums[left] + nums[right] + num
                    distance_to_target = current_distance_to_target
                
                if nums[left] + nums[right] < sum_left_right:
                    left += 1
                elif nums[left] + nums[right] > sum_left_right:
                    right -= 1
                else:
                    return target

        return best_fitting_sum




 
        
Sol = Solution()
#nums = [-1,2,1,-4] #, 1 -> 2
#nums = [1,-3,3,5,4,1] # , 1, -> 1
#nums = [0, 2, 1, -3] #, 1-> 0
#nums = [0, 0, 0] #, 1 -> 0
nums = [-1,0,1,2,-1,-4] #, 0 -> 0




print(Sol.threeSumClosest(nums, 0))
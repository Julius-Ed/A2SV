class Solution:
    def twoSum(self, nums, target):
        
        counting_dict = {}

        for index, num in enumerate(nums):
            
            if num not in counting_dict:
                counting_dict[num] = [index]
            else:
                counting_dict[num].append(index)
        
        for index, num in enumerate(nums):

            look_up_val = target - num

            if look_up_val in counting_dict:
                if look_up_val != num:
                    indices =  counting_dict[look_up_val]
                    indices.append(index)
                    return indices
                elif len(counting_dict[look_up_val]) > 1:
                    return counting_dict[look_up_val]
        
        return False





Sol = Solution()
print(Sol.twoSum([3, 3], 6))



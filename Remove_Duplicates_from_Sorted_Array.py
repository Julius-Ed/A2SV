class Solution:
    def removeDuplicates(self, nums) -> int:
        
        

        index = 0
        while index < len(nums) - 1:

            val = nums[index]

            if nums[index] == nums[index + 1]:

                index += 1
                while index < len(nums) and nums[index] == val:
                    nums[index] = 101
                    index += 1
            else:
                index += 1
        
        nums.sort()

        k = 0
        for num in nums:
            if num < 101:
                k += 1

        return k
            




Sol = Solution()


nums = [0,0,1,1,1,2,2,3,3,4]

print(Sol.removeDuplicates(nums))
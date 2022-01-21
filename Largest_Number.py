

class Solution:
    def largestNumber(self, nums):
        
        for i in range(len(nums)):
            nums[i] = str(nums[i])

        for _ in nums:
            for index in range(len(nums) - 1):

                option_a = nums[index] + nums[index + 1]
                option_b = nums[index + 1] + nums[index]

                if int(option_a) < int(option_b):
                    nums[index], nums[index + 1] = nums[index + 1], nums[index]
        
        result = ""

        for num in nums:
            result += num
        
        if result[0] == "0":
            return "0"

        return result


Sol = Solution()
print(Sol.largestNumber([3,30,34,5,9]))
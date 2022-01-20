
class Solution:
    def sortColors(self, nums) -> None:

        acc = [0, 0, 0]

        for color in nums:
            acc[color] += 1

        start = 0
        for color in range(len(acc)):

            for index in range(start, start + acc[color]):
                nums[index] = color
            start += acc[color]

Sol = Solution()

class Dutch:

    def sortColors(self, nums):

        i = 0
        zero_pointer = 0
        two_pointer = len(nums) - 1

        while i < len(nums):
            
            if nums[zero_pointer] == 0:
                nums[zero_pointer], nums[i] = nums[i], nums[zero_pointer]
                zero_pointer += 1
                i += 1
            elif nums[zero_pointer] == 1:
                i += 1
            else: # zero pointer hitting a 2
                nums[zero_pointer], nums[two_pointer] = nums[two_pointer], nums[zero_pointer]
                two_pointer -= 1
        
        print(nums)


nums = [2, 0, 2, 1, 1, 0]


Du = Dutch()
Du.sortColors(nums)
Sol.sortColors(nums)

"""
Array With Elements Not Equal to Average of Neighbors
"""

class Solution:
    def rearrangeArray(self, nums):
        
        nums.sort()

        if len(nums) % 2 != 0:
            median = nums[len(nums) // 2]
        else:
            median = (nums[(len(nums) // 2) - 1] + nums[(len(nums) // 2)]) / 2
        
        
        smallerOrMedian = []
        greater = []

        for num in nums:
            if num <= median:
                smallerOrMedian.append(num)
            else:
                greater.append(num)
        

        i = 0
        while smallerOrMedian and greater:
            nums[i] = smallerOrMedian.pop()
            nums[i + 1] = greater.pop()

            i += 2
        
        if smallerOrMedian:
            nums[-1] = smallerOrMedian.pop()

        return nums


Sol = Solution()


print(Sol.rearrangeArray([0, 2, 6, 7, 9, 10]))
print(Sol.rearrangeArray([1, 2, 3, 4, 5]))
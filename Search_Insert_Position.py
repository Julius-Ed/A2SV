class Solution:
    def searchInsert(self, nums, target) -> int:
    

        low = 0
        high = len(nums)

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
                return mid


        return low

nums = [1,3,5,6]
target = 2


Sol = Solution()
print(Sol.searchInsert(nums, target))
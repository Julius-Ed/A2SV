from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        nums.append(0)
        left, right = 0, 0
        acc = 0
        result = float('inf')

        while right < len(nums) and left <= right:

            if acc < target:
                acc += nums[right]
                right += 1
            else:
                result = min(right - left, result)
                acc -= nums[left]
                left += 1

        if result == float('inf'):
            return 0

        return result


Sol = Solution()
print(Sol.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]) == 2)
print(Sol.minSubArrayLen(4, [1, 4, 4]) == 1)

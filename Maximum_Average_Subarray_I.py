from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        left, right = 0, k - 1
        totalWindow = sum(nums[:right + 1])
        result = totalWindow / k

        while right < len(nums) - 1:

            totalWindow -= nums[left]

            left += 1
            right += 1

            totalWindow += nums[right]

            result = max(result, totalWindow / k)

        return result


Sol = Solution()
print(Sol.findMaxAverage([1, 12, -5, -6, 50, 3], 4))
print(Sol.findMaxAverage([5], 1))

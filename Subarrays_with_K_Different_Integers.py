from typing import List


class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:

        counter = 0
        left = 0
        right = 0

        window = {}

        while right < len(nums):

            if nums[right] in window:
                window[nums[right]] += 1
            else:
                window[nums[right]] = 1

            while len(window) > k:
                if window[nums[left]] == 1:
                    window.pop(nums[left])
                else:
                    window[nums[left]] -= 1

                left += 1

            right += 1

            if len(window) == k:
                counter += 1

        return counter


Sol = Solution()
print(Sol.subarraysWithKDistinct([1, 2, 1, 2, 3], 2))

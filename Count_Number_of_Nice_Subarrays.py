from typing import List
from collections import defaultdict


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:

        res = 0

        for i, num in enumerate(nums):
            if num % 2 == 0:
                nums[i] = 0
            else:
                nums[i] = 1

        acc = 0
        for i, num in enumerate(nums):
            acc += num
            nums[i] = acc

        lookUps = defaultdict(int)

        nums = [0] + nums

        for num in nums:
            lookUp = num - k
            if lookUp in lookUps:
                res += lookUps[lookUp]
            lookUps[num] += 1
    
        return res


Sol = Solution()
print(Sol.numberOfSubarrays([1, 1, 2, 1, 1], 3))
print(Sol.numberOfSubarrays([1,1,1,1,1], 1))

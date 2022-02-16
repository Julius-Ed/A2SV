from typing import List

from sqlalchemy import true


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:

        if len(nums) < 2:
            return False

        moduloDictionary = {}
        acc = 0
        for numIndex, num in enumerate(nums):
            acc += num
            if acc % k == 0 and numIndex != 0:
                return True
            elif acc % k in moduloDictionary:
                moduloDictionary[acc % k] += [numIndex]
            else:
                moduloDictionary[acc % k] = [numIndex]

        for candidate in moduloDictionary:
            if len(moduloDictionary[candidate]) >= 2:
                if moduloDictionary[candidate][-1] - moduloDictionary[candidate][0] > 1:
                    return True

        if sum(nums) % k == 0:
            return True

        return False


Sol = Solution()
print(Sol.checkSubarraySum([23, 2, 4, 6, 7], 6) == True)
print(Sol.checkSubarraySum([23, 2, 6, 4, 7], 13) == False)
print(Sol.checkSubarraySum([23, 2, 4, 6, 6], 7) == True)
print(Sol.checkSubarraySum([1, 2, 3], 5) == True)

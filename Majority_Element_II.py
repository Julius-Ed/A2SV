from typing import List
from collections import Counter


class SolutionLinearSpace:
    def majorityElement(self, nums: List[int]) -> List[int]:

        countingDict = Counter(nums)
        res = []
        for num in countingDict:
            if countingDict[num] > len(nums) / 3:
                res.append(num)

        return res

# note that there can be at most two such elements.
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        res = []

        cand0, cand1 = 0, 1
        count0, count1 = 0, 0

        for num in nums:

            if num == cand0:
                count0 += 1

            elif num == cand1:
                count1 += 1

            elif count0 == 0:
                cand0, count0 = num, 1

            elif count1 == 0:
                cand1, count1 = num, 1

            else:
                count0, count1 = count0 - 1, count1 - 1

        count0, count1 = 0, 0

        for num in nums:
            if num == cand0:
                count0 += 1

            if num == cand1:
                count1 += 1

        if count0 > len(nums) // 3:
            res.append(cand0)

        if count1 > len(nums) // 3:
            res.append(cand1)

        return res


Sol = Solution()
print(Sol.majorityElement([3, 2, 3]))

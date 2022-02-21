from typing import List

class Solution:
    def bestRotation(self, nums: List[int]) -> int:
        
        length = len(nums)
        ranges = [0] * length

        for index, val in enumerate(nums):

            leftK = (index - val + 1) % length
            rightK = (index + 1) % length

            ranges[leftK] -= 1
            ranges[rightK] += 1

            if leftK > rightK:
                ranges[0] -= 1
        
        acc = 0
        for index, val in enumerate(ranges):
            acc += val
            ranges[index] = acc

        maxK = float('-inf')
        maxKIndex = - 1

        for index, val in enumerate(ranges):
            if val > maxK:
                maxK = val
                maxKIndex = index
        
        return maxKIndex

Sol = Solution()
print(Sol.bestRotation([2, 3, 1, 4, 0]))

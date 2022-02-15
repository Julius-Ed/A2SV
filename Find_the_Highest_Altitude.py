from typing import List

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        
        acc = 0
        for index, slope in enumerate(gain):
            acc += slope
            gain[index] = acc

        maxGain = max(gain)

        return max(0, maxGain)

Sol = Solution()
print(Sol.largestAltitude([-5,1,5,0,-7]) == 1)
print(Sol.largestAltitude([-4,-3,-2,-1,4,3,2]) == 0)
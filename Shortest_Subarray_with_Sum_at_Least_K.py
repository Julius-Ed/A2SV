
from typing import List

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        
        sumStack = []
        sumOfStack = 0

        result = float('inf')

        for num in nums:
            
            sumStack.append(num)
            sumOfStack += num

            popCounter = 0
            popSum = 0

            if sumOfStack <= 0:
                sumStack = []
                sumOfStack = 0
                
            elif sumOfStack >= k:
                while sumStack and popSum < k:
                    popSum += sumStack.pop()
                    popCounter += 1
                
                sumStack = []
                sumOfStack = 0
            
    
                result = min(result, popCounter)
            
        if result == float('inf'): return -1
        else: return result


Sol = Solution()
# print(Sol.shortestSubarray([2, -1, 2, 1, 2], 8))
# print(Sol.shortestSubarray([17,85,93,-45,-21], 150))
# print(Sol.shortestSubarray([1], 1))

print(Sol.shortestSubarray([56, -21, 56, 35, -9], 61) == 2)
from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        sumDictionary = {0: 1}
        sumArray = []
        resultCounter = 0
        precedingSum = 0


        for num in nums:
            precedingSum += num
            sumArray.append(precedingSum)

            if precedingSum - k in sumDictionary:
                resultCounter += sumDictionary[precedingSum - k]
    
            if precedingSum in sumDictionary:
                sumDictionary[precedingSum] += 1
            else:
                sumDictionary[precedingSum] = 1
        
        return resultCounter



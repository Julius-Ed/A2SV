from typing import List

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        res = 0
        left = 0
        right = 0

        window = {}
        windowLength = 0
        
        if len(set(fruits)) <= 2:
            return len(fruits)

        while right < len(fruits):   
            
            if fruits[right] not in window:
                window[fruits[right]] = 1
            else:
                window[fruits[right]] += 1
            
            while len(window) > 2:
                windowLength -= 1
                if window[fruits[left]] == 1:
                    window.pop(fruits[left])
                else:
                    window[fruits[left]] -= 1
            
                left += 1
    
            right += 1
            windowLength += 1
            
            if len(window) == 2:
                res = max(res, windowLength)


        return res

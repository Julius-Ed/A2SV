from typing import List

class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:

        if len(set(arr)) == 1:
            return 1

        conv = []

        for index in range(len(arr) - 1):
            
            if arr[index] > arr[index + 1]:
                conv.append(1)
            elif arr[index] < arr[index + 1]:
                conv.append(-1)
            else:
                conv.append(0)
        
        conv.append(0)
        

        res = 2
        left, right = -1, 0

        while right < len(conv):

            moved = False
            while right + 1 < len(conv) and abs(conv[right] - conv[right + 1]) > 1:
                right += 1
                moved = True

            if moved:
                res = max(res, right - left + 1)
            left = right
            right += 1

        return res


Sol = Solution()

from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        valuesInWindow = set()
        valuesInWindow.add(nums[0])

        left, right = 0, 0

        while right < len(nums) - 1:

            if right - left >= k:
                valuesInWindow.remove(nums[left])
                left += 1
            
            else:

                if nums[right + 1] in valuesInWindow:
                    return True
                else:
                    valuesInWindow.add(nums[right + 1])
        
                right += 1
        
        return False



Sol = Solution()

print(Sol.containsNearbyDuplicate([1, 2, 3, 1], 3) == True)
print(Sol.containsNearbyDuplicate([1, 0, 1, 1], 1) == True)
print(Sol.containsNearbyDuplicate([1,2,3,1,2,3], 2) == False)


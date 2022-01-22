
"""
Find Original Array From Doubled Array
"""

from collections import Counter


class Solution:
    def findOriginalArray(self, changed):

        if len(changed) <= 1:
            return []
        
        if len(changed) % 2 != 0:
            return []
    
        changed.sort()

        result = []

        my_dict = Counter(changed)

        for i in range(len(changed)):

            num = changed[i]
            duplicate = num * 2

            if my_dict[num] == 0:
                continue

            if my_dict[duplicate] > 0:
                result.append(num)
                my_dict[duplicate] -= 1
                my_dict[num] -= 1
            else:
                return []

        return result


Sol = Solution()

print(Sol.findOriginalArray([1, 2, 3, 4, 6, 8]))
print(Sol.findOriginalArray([0, 0, 0, 0]))

print(Sol.findOriginalArray([4, 2, 0]))

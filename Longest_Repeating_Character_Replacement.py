

from turtle import right


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        
        count = {}
        res = 0

        left = 0

        for right in range(len(s)):

            count[s[right]] = 1 + count.get(s[right], 0)

            while (right - left + 1) - max(count.values()) > k:
                count[s[left]] -= 1
                left += 1

            res = max(res, right - left + 1)
    
        return res



Sol = Solution()
print(Sol.characterReplacement("ABAB", 2) == 4)
print(Sol.characterReplacement("AABABBA", 1))
# print(Sol.characterReplacement("ABAA", 0))
# print(Sol.characterReplacement("ABBB", 2))

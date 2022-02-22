class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        seen = {}

        left, right = 0, 0
        res = 0

        while right < len(s):

            if s[right] not in seen:
                seen[s[right]] = right
                res = max(res, right - left + 1)
            elif seen[s[right]] < left:
                res = max(res, right - left + 1)
            
            else:
                left = seen[s[right]] + 1
            
            seen[s[right]] = right
            right += 1

        return res

Sol = Solution()
print(Sol.lengthOfLongestSubstring("pwwkew") == 3)
print(Sol.lengthOfLongestSubstring(" ") == 1)
print(Sol.lengthOfLongestSubstring("dvdf") == 3)

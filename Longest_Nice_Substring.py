
class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if len(s) == 0:
            return ""

        lookupValues = set(s)

        for index, character in enumerate(s):

            if character.isupper() and character.lower() not in lookupValues or character.islower() and character.upper() not in lookupValues:
                left = self.longestNiceSubstring(s[:index])
                right = self.longestNiceSubstring(s[index + 1:])

                if len(left) >= len(right):
                    return left
                else:
                    return right
        return s




Sol = Solution()
print(Sol.longestNiceSubstring("YazaAay"))
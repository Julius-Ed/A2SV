from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        boolArray = [False] * (len(s) + 1)
        boolArray[-1] = True

        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:

                if (i + len(w)) <= len(s) and s[i:i+len(w)] == w:
                    boolArray[i] = boolArray[i + len(w)]

                if boolArray[i] == True:
                    break

        return boolArray[0]

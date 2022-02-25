from typing import List
from collections import deque


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        digitDictionary = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

        if len(digits) == 1:
            return digitDictionary[digits[0]]

        if len(digits) == 0:
            return []

        digitStack = deque(digits)

        firstRound = True
        while len(digitStack) > 1:

            first = digitStack.popleft()
            second = digitStack.popleft()
            if firstRound:
                new = self.combine(digitDictionary[first], digitDictionary[second])
                firstRound = False
            else:
                new = self.combine(first, digitDictionary[second])
    
            digitStack.appendleft(new)

        return digitStack[0]

    def combine(self, listA, listB):

        res = []

        for charA in listA:
            for charB in listB:
                res.append(charA + charB)

        return res


Sol = Solution()
print(Sol.letterCombinations("2"))

from typing import List
from collections import deque


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:

        counter = {}
        runningWindow = deque(s[:10])

        counter["".join(runningWindow)] = 1

        right = 10

        while right < len(s):
            runningWindow.popleft()
            runningWindow.append(s[right])

            sequence = "".join(runningWindow)

            if sequence in counter:
                counter[sequence] += 1
            else:
                counter[sequence] = 1

            right += 1

        res = []

        for sequence in counter:
            if counter[sequence] > 1:
                res.append(sequence)

        return res


Sol = Solution()
print(Sol.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))

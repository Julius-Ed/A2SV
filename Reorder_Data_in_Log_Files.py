from typing import List


"""
The letter-logs come before all digit-logs.
The letter-logs are sorted lexicographically by their contents. If their contents are the same, then sort them lexicographically by their identifiers.
The digit-logs maintain their relative ordering.
"""


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:

        letterLogs, digitLogs = [], []

        for log in logs:
            if log[-1].isalpha():
                letterLogs.append(log)
            else:
                digitLogs.append(log)

        # first sort by identifiers
        letterLogs.sort(key=lambda x: x.split()[0])
        # then sort by contents
        letterLogs.sort(key=lambda x: x.split()[1:])

        res = letterLogs + digitLogs

        return res


Sol = Solution()
logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6",
        "let2 own kit dig", "let3 art zero"]

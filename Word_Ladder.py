
from typing import List
from collections import deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        # create adjacency list
        childrenDict = {}
        for word in wordList:
            wordListified = list(word)
            for index, w in enumerate(wordListified):

                # create wildcard on all positions.
                wordListified[index] = "*"
                encodedWord = "".join(wordListified)
                wordListified[index] = w

                if encodedWord not in childrenDict:
                    childrenDict[encodedWord] = set()

                # map words with wildcards to actual words
                childrenDict[encodedWord].add(word)

        visited = set()
        q = deque([(beginWord, 1)])

        while q:
            word, level = q.popleft()

            children = self.findChildren(word, childrenDict)

            for child in children:

                if child == endWord:
                    return level + 1

                if child not in visited:
                    visited.add(child)
                    q.append((child, level + 1))

        return 0

    def findChildren(self, word, childrenDict):

        res = []

        wordListified = list(word)
        for index, w in enumerate(wordListified):

            wordListified[index] = "*"
            encodedWord = "".join(wordListified)
            wordListified[index] = w

            if encodedWord not in childrenDict:
                continue
            for ele in childrenDict[encodedWord]:
                res.append(ele)

        return res


Sol = Solution()
print(Sol.ladderLength('hit', 'cog', [
      "hot", "dot", "dog", "lot", "log", "cog"]))

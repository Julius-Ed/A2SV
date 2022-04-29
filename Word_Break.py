from typing import List
from collections import deque


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        myTrie = Trie()

        for word in wordDict:
            myTrie.addWord(word)

        q = deque([(s, "")])

        reachable = [0] * len(s)
        reachable[len(s)] = 1

        for i in range(len(s) - 1, -1, -1):
            pass
        # while q:

        #     notCov, cov = q.popleft()

        #     for i in range(1, len(notCov) + 1):

        #         if myTrie.wordExists(notCov[:i]):
        #             newNotCov, newCov = (notCov[i:], cov + notCov[:i])
        #             q.append((newNotCov, newCov))

        #             if len(s) == len(newCov):
        #                 return True

        # return False


class TrieNode:

    def __init__(self, end=False, wordLength=0):
        self.isEnd = end
        self.children = [None] * 26
        self.wordLength = wordLength


class Trie:

    def __init__(self) -> None:
        self.root = TrieNode()

    def addWord(self, word):

        curr = self.root

        for pos, c in enumerate(word):
            i = ord(c) - ord("a")
            # add new node if character doesnt exist yet.
            if not curr.children[i]:
                curr.children[i] = TrieNode(wordLength=pos + 1)

            curr = curr.children[i]

        curr.isEnd = True

    def wordExists(self, word):
        curr = self.root

        res = []

        for c in word:
            i = ord(c) - ord("a")

            if not curr.children[i]:
                return False

            curr = curr.children[i]

        return curr.isEnd


Sol = Solution()
s = "leetcode"
wordDict = ["leet", "code"]
print(Sol.wordBreak(s, wordDict) == True)


# print(Sol.wordBreak("abcd", ["a", "abc", "b", "cd"]))

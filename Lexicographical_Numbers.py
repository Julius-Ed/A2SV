from typing import List


class TrieNode:

    def __init__(self, isEnd=False):

        self.children = {}
        self.isEnd = isEnd


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def addNum(self, num):

        curr = self.root

        for c in num:

            if c not in curr.children:
                curr.children[c] = TrieNode()

            curr = curr.children[c]

        curr.isEnd = True

    def traverseTrie(self):
        res = []

        curr = self.root

        def dfs(curr, prefix):

            if len(curr.children) == 0:
                return

            res.add()

            for child in curr.children:
                pass  # CALL


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        pass


Sol = Solution()

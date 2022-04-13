
from typing import Node


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def maxDepth(self, root: 'Node') -> int:

        if not root:
            return 0

        self.res = 0

        def dfs(curr, depth):

            if not curr:
                return

            if depth > self.res:
                self.res = depth

            for child in curr.children:
                dfs(child, depth + 1)

        dfs(root, 1)

        return self.res


Sol = Solution()

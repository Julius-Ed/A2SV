# Definition for a binary tree node.

from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:

        self.total = 0

        def dfs(curr, path):

            if curr and not curr.left and not curr.right:
                self.total += int(path + str(curr.val), 2)

            if not curr:
                return

            dfs(curr.left, path + str(curr.val))
            dfs(curr.right, path + str(curr.val))

        dfs(root, "")

        return self.total


Sol = Solution()

root = TreeNode(1)

root.left = TreeNode(0)
root.right = TreeNode(1)

root.left.left = TreeNode(0)
root.left.right = TreeNode(1)

root.right.left = TreeNode(0)
root.right.right = TreeNode(1)


print(Sol.sumRootToLeaf(root))

# Definition for a binary tree node.

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        self.res = 0

        def dfs(curr, depth):

            if not curr:
                return

            if depth > self.res:
                self.res = depth
            dfs(curr.left, depth + 1)
            dfs(curr.right, depth + 1)

        dfs(root, 0)
        print(self.res)


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)

root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

Sol = Solution()
print(Sol.maxDepth(root))

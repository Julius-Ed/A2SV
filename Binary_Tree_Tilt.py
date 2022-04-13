# Definition for a binary tree node.
from turtle import left, right
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:

        self.totalTilt = 0

        def dfs(curr):

            if not curr:
                return 0

            leftSubTree = dfs(curr.left)
            rightSubTree = dfs(curr.right)

            self.totalTilt += abs(leftSubTree - rightSubTree)

            return leftSubTree + rightSubTree + curr.val

        dfs(root)
        return self.totalTilt


root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(9)

root.left.left = TreeNode(3)
root.left.right = TreeNode(5)

root.right.right = TreeNode(7)


Sol = Solution()
print(Sol.findTilt(root))

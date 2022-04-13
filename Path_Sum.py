# Definition for a binary tree node.
from typing import Optional

from regex import R


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        if not root:
            return False

        pathSums = set()

        def dfs(curr, currentSum):

            if curr and not curr.left and not curr.right:
                pathSums.add(currentSum + curr.val)

            if not curr:
                return

            dfs(curr.left, currentSum + curr.val)
            dfs(curr.right, currentSum + curr.val)

        dfs(root, 0)

        return targetSum in pathSums


Sol = Solution()

root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(11)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right.right.right = TreeNode(1)

print(Sol.hasPathSum(root, 22))

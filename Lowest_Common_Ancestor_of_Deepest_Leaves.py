from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        self.res = root
        self.maxLevel = 0

        # traverse through binary tree.
        def dfs(curr, level):

            self.maxLevel = max(self.maxLevel, level)

            if not curr:
                return level

            leftHeight = dfs(curr.left, level + 1)
            rightHeight = dfs(curr.right, level + 1)

            # if left and right tree have the same height current node is a candidate.
            if leftHeight == rightHeight == self.maxLevel:
                self.res = curr

            return max(leftHeight, rightHeight)

        dfs(root, 0)
        return self.res


Sol = Solution()

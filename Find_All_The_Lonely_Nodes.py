from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return

        res = []

        def dfs(curr):

            if not curr:
                return

            dfs(curr.left)

            if curr.left and not curr.right:
                res.append(curr.left.val)
            elif curr.right and not curr.left:
                res.append(curr.right.val)

            dfs(curr.right)

        dfs(root)
        return res


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(4)

Sol = Solution()
print(Sol.getLonelyNodes(root))

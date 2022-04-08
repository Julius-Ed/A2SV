from typing import Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        return self.invertVals(root.left, True) == self.invertVals(root.right, False)

    def invertVals(self, root, rev):

        if not root:
            return []

        q, sameLevelVals = deque([(root, 0)]), deque([root.val])
        prevLevel, res = -1, []

        while q:

            curr, level = q.popleft()

            # if a new level is started append collection of values to the result.
            if level > prevLevel:
                if prevLevel != -1:
                    res.append(list(sameLevelVals))

                prevLevel = level
                sameLevelVals = deque([])

            if curr and rev:
                sameLevelVals.appendleft(curr.val)
            elif curr:
                sameLevelVals.append(curr.val)
            elif rev:
                sameLevelVals.appendleft(None)
            else:
                sameLevelVals.append(None)

            if curr:
                q.append((curr.left, level + 1))
                q.append((curr.right, level + 1))

        # note that same Level has remaining values not included in the result mass.
        res.append(list(sameLevelVals))

        return res


# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(2)

# root.left.left = TreeNode(3)
# root.left.right = TreeNode(4)

# root.right.left = TreeNode(4)
# root.right.right = TreeNode(3)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)


root.left.right = TreeNode(3)
root.right.right = TreeNode(3)


Sol = Solution()
print(Sol.isSymmetric(root))

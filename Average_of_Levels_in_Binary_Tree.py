from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:

        res = []

        prevLevel, accLevel, nodeCountLevel = 0, 0, 0

        q = deque([(root, 0)])

        while q:

            curr, level = q.popleft()

            if level > prevLevel:
                prevLevel += 1

                if accLevel == 0:
                    res.append(0)
                else:
                    res.append(accLevel / nodeCountLevel)

                accLevel = curr.val
                nodeCountLevel = 1

            else:
                accLevel += curr.val
                nodeCountLevel += 1

            if curr.left:
                q.append((curr.left, level + 1))

            if curr.right:
                q.append((curr.right, level + 1))

        res.append(accLevel / nodeCountLevel)

        return res


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)

root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

# root = TreeNode(0)
# root.left = TreeNode(-1)

Sol = Solution()
print(Sol.averageOfLevels(root))

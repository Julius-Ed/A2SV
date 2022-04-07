from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # O(number of nodes in tree)
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:

        res = []

        prevLevel, accLevel, nodeCountLevel = 0, 0, 0

        # save nodes as tuples with node object on index 0 and level on index 1.
        q = deque([(root, 0)])

        while q:
            curr, level = q.popleft()

            # calcualte average whenever we reach a new level.
            if level > prevLevel:
                prevLevel += 1

                # avoid devision by 0.
                if accLevel == 0:
                    res.append(0)
                else:
                    res.append(accLevel / nodeCountLevel)

                accLevel = curr.val
                nodeCountLevel = 1

            # update running sums if we don't reach a new level.
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


from typing import List, Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Time Complexity: O(Number of Nodes)
    # Space Complexity: O(1)
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if root is None:
            return []

        res = []
        prevLevel, prevVal = -1, -1
        q = deque([(root, 0)])

        while q:

            curr, level = q.popleft()

            # whenever a new level starts, append to result the last node from the previous level.
            if level > prevLevel:
                if prevLevel != -1:
                    res.append(prevVal)
                prevLevel = level

            if curr.left:
                q.append((curr.left, level + 1))

            if curr.right:
                q.append((curr.right, level + 1))

            prevVal = curr.val

        res.append(curr.val)
        return res

# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
# root.left.right = TreeNode(5)
# root.right.left = TreeNode(10)
# root.right.left.right = TreeNode(11)

# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
# root.left.right = TreeNode(5)
# root.right.right = TreeNode(4)


root = TreeNode(1)
root.right = TreeNode(3)
root.left = TreeNode(2)
root.left.left = TreeNode(4)

Sol = Solution()
print(Sol.rightSideView(root))

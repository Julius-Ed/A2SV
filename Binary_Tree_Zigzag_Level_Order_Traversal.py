
from typing import Optional, List
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

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

            # if we are on an odd level, append from the left to reverse the nodes.
            if level % 2 != 0:
                sameLevelVals.appendleft(curr.val)
            else:
                sameLevelVals.append(curr.val)

            # add left and right children to the queue.
            if curr.left:
                q.append((curr.left, level + 1))

            if curr.right:
                q.append((curr.right, level + 1))

        # note that same Level has remaining values not included in the result mass.
        res.append(list(sameLevelVals))

        return res


# root = TreeNode(3)
# root.left = TreeNode(9)
# root.right = TreeNode(20)

# root.right.left = TreeNode(15)
# root.right.right = TreeNode(7)


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

Sol = Solution()
print(Sol.zigzagLevelOrder(root))

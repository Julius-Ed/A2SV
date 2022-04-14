# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        res = 0

        q = deque([root])

        while q:
            curr = q.popleft()

            if curr.val % 2 == 0:
                res += self.getGrandChildren(curr)

            if curr.left:
                q.append(curr.left)

            if curr.right:
                q.append(curr.right)

        return res

    def getGrandChildren(self, grandpa):

        totalSum = 0

        q = deque([(grandpa, 0)])

        while q:
            curr, level = q.popleft()

            if level == 2:
                totalSum += curr.val

            if level < 2 and curr.left:
                q.append((curr.left, level + 1))

            if level < 2 and curr.right:
                q.append((curr.right, level + 1))

        return totalSum


Sol = Solution()


root = TreeNode(6)
# root.left = TreeNode(7)
# root.right = TreeNode(8)

# root.left.left = TreeNode(2)
# root.left.right = TreeNode(7)

# root.left.left.left = TreeNode(9)

# root.left.right.left = TreeNode(1)
# root.left.right.right = TreeNode(4)


# root.right.left = TreeNode(1)
# root.right.right = TreeNode(3)

# root.right.right.right = TreeNode(5)


print(Sol.sumEvenGrandparent(root))

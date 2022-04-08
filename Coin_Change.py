from typing import List
from collections import deque


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        visitedAmounts = set()

        if amount == 0:
            return 0

        q = deque([(0, 0)])

        while q:

            currAmount, level = q.popleft()

            for coin in coins:
                newAmount = currAmount + coin
                if newAmount == amount:
                    return level + 1
                elif newAmount < amount and newAmount not in visitedAmounts:
                    visitedAmounts.add(newAmount)
                    q.append((newAmount, level + 1))

        return -1


Sol = Solution()
print(Sol.coinChange([1, 2, 5], 11))

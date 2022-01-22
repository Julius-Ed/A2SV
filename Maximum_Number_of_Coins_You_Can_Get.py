

from collections import deque

class Solution:
    def maxCoins(self, piles) -> int:
        
        piles.sort(reverse = True)

        q = deque(piles)

        coins = 0

        while q: 

            q.popleft()
            me = q.popleft()
            q.pop()

            coins += me

        return coins


Sol = Solution()

#piles = [9,8,7,6,5,1,2,3,4]
#piles = [2,4,1,2,7,8]

print(Sol.maxCoins(piles))
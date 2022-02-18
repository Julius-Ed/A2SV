from typing import List
from random import choices


class Solution:

    def __init__(self, w: List[int]):
        self.distribution = []
        self.indices = [i for i in range(len(w))]

        totalWeight = sum(w)
        for weight in w:
            self.distribution.append(weight/totalWeight)

    def pickIndex(self) -> int:

        return choices(self.indices, self.distribution, k=1)[0]


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()

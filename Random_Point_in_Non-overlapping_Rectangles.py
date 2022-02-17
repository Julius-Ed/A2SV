from typing import List

from random import randint, random, randrange, choices
from numpy.random import choice


class Solution:

    def __init__(self, rects: List[List[int]]):
        self.areas = []
        self.probabilityDistribution = []
        self.ranges = []

        for rect in rects:
            self.areas.append(
                (abs(rect[0] - rect[2]) + 1) * (abs(rect[1] - rect[3]) + 1))
            self.ranges.append([(rect[0], rect[2]), (rect[1], rect[3])])

        totalArea = sum(self.areas)

        for area in self.areas:
            self.probabilityDistribution.append(area/totalArea)

        self.indices = [i for i in range(len(self.areas))]

    def pick(self) -> List[int]:

        # 1. randomly select the rectangle based on the area.
        drawIndex = choices(population=self.indices, k=1,
                            weights=self.probabilityDistribution)[0]

        # 2. given the rectangle, randmomly select a coordinate based on its ranges.
        xValue = randint(min(self.ranges[drawIndex][0][0], self.ranges[drawIndex][0][1]), max(
            self.ranges[drawIndex][0][0], self.ranges[drawIndex][0][1]))
        yValue = randint(min(self.ranges[drawIndex][1][0], self.ranges[drawIndex][1][1]), max(
            self.ranges[drawIndex][1][0], self.ranges[drawIndex][1][1]))

        return [xValue, yValue]



# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()

Sol = Solution([[-2, 5, -2, 1], [2, 4, 4, 4]])
print(Sol.pick())
print(Sol.pick())
print(Sol.pick())
print(Sol.pick())
print(Sol.pick())


"""
["Solution","pick","pick","pick","pick","pick"]
[[[[-2,-2,1,1],[2,2,4,6]]],[],[],[],[],[]]
"""

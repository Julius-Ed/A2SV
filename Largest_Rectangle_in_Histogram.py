from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        maxArea = 0
        heightStack = []

        for heightsIndex, heightsHeight in enumerate(heights):
            start = heightsIndex

            while heightStack and heightStack[-1][1] > heightsHeight:
                index, height = heightStack.pop()
                maxArea = max(maxArea, height * (heightsIndex - index))
                start = index
            heightStack.append((start, heightsHeight))

        for heightsIndex, heightsHeight in heightStack:
            maxArea = max(maxArea, heightsHeight * (len(heights) - heightsIndex))

        return maxArea


Sol = Solution()


print(Sol.largestRectangleArea([2, 1, 5, 6, 3]))

#print(Sol.largestRectangleArea([1, 2, 3, 4, 5, 6]))

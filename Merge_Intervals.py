class Solution:
    def merge(self, intervals):

        intervals.sort()

        i = 0
        while i < len(intervals) - 1:

            if intervals[i][0] <= intervals[i + 1][0] and intervals[i][1] >= intervals[i + 1][1]:
                intervals.pop(i + 1)
                i -= 1

            elif intervals[i][1] >= intervals[i + 1][0]:
                intervals[i + 1] = [intervals[i][0], intervals[i + 1][1]]
                intervals.pop(i)

                i -= 1

            i += 1

        return intervals


Sol = Solution()


intervals = [[2, 6], [8, 10], [15, 18], [1, 3]]
intervals_2 = [[1, 4], [4, 5]]
intervals_3 = [[1, 4], [2, 3]]

print(Sol.merge(intervals))
print(Sol.merge(intervals_2))
print(Sol.merge(intervals_3))

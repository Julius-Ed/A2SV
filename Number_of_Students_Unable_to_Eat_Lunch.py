from collections import deque
from typing import List


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:

        sadwichesStack = deque(sandwiches)
        studentQueue = deque(students)

        lengthStudentQueue = len(studentQueue)
        sumOfPrefernces = sum(studentQueue)

        sumSandwichStack = sum(sadwichesStack)

        while len(studentQueue) > 0 and len(sadwichesStack) > 0:

            if sadwichesStack[0] == studentQueue[0]:
                lengthStudentQueue -= 1
                sumOfPrefernces -= studentQueue[0]
                sumSandwichStack -= sadwichesStack[0]

                sadwichesStack.popleft()
                studentQueue.popleft()

            elif (sumOfPrefernces == lengthStudentQueue) or (sumOfPrefernces == 0):
                return lengthStudentQueue
            else:
                studentQueue.append(studentQueue.popleft())

        return lengthStudentQueue


Sol = Solution()

"""
# Definition for Employee.
"""

from typing import List
from collections import deque


class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates


# Given an integer id that represents an employee's ID, return the total importance value of this employee
# and all their direct and indirect subordinates.
class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:

        empIds = {}

        # map employee IDs to employee objects
        for emp in employees:
            if emp.id not in empIds:
                empIds[emp.id] = emp

        if id not in empIds:
            return

        q, res = deque([id]), 0

        while q:

            id = q.popleft()
            employee = empIds[id]

            res += employee.importance

            # mark as visited but setting importance to -101
            employee.importance = -101

            for subId in employee.subordinates:
                if empIds[subId].importance != -101:
                    q.append(subId)

        return res

    def getImportanceDFS(self, employees: List['Employee'], id: int) -> int:

        empIds = {}

        # map employee IDs to employee objects
        for emp in employees:
            if emp.id not in empIds:
                empIds[emp.id] = emp

        self.res = 0

        def dfs(id):

            self.res += empIds[id].importance

            for subId in empIds[id].subordinates:
                dfs(subId)

        dfs(id)
        return self.res


Sol = Solution()


id1 = Employee(1, 5, [2, 3])
id2 = Employee(2, 3, [])
id3 = Employee(3, 3, [])

print(Sol.getImportanceDFS([id1, id2, id3], 1))
print(Sol.getImportance([id1, id2, id3], 1))

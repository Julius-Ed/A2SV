from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        positionsAndSpeed = []
        fleetCounter = 0

        for carPosition, carSpeed in zip(position, speed):
            positionsAndSpeed.append((carPosition, carSpeed))
        
        positionsAndSpeed.sort()
        carStack = positionsAndSpeed



        while carStack:
            while len(carStack) > 1:

                deltaMiles = carStack[-1][0] - carStack[-2][0]
                deltaSpeed = carStack[-2][1] - carStack[-1][1]

                if deltaSpeed <= 0:
                    break

                catchUpTime = deltaMiles / deltaSpeed
                meetingPoint = catchUpTime * carStack[-1][1] + carStack[-1][0]

                if meetingPoint <= target:

                    if carStack[-2][1] > carStack[-1][1]:
                        carStack.pop(-2)
                    else:
                        carStack.pop()
                else:
                    break
            carStack.pop()
            fleetCounter += 1

        return fleetCounter




Sol = Solution()

print(Sol.carFleet(12, [10,8,0,5,3], [2,4,1,1,3]) == 3)
print(Sol.carFleet(10, [3], [3]) == 1)
print(Sol.carFleet(100, [0, 2, 4], [4, 2, 1]) == 1)
print(Sol.carFleet(10, [6, 8], [3, 2]) == 2)
print(Sol.carFleet(10, [0, 4, 2], [2, 1, 3]) == 1)


class Solution:
    def dailyTemperatures(self, temperatures):
        temperatureStack = [[temperatures[0], 0]]
        result = [0] * len(temperatures)


        for tempIndex in range(1, len(temperatures)):
            temperature = temperatures[tempIndex]

            if temperature <= temperatureStack[-1][0]:
                temperatureStack.append([temperature, tempIndex])
            else:

                while temperatureStack and temperature > temperatureStack[-1][0]:
                    
                    prevTemperature, prevIndex = temperatureStack.pop()
                    result[prevIndex] = tempIndex - prevIndex
                
                temperatureStack.append([temperature, tempIndex])

        return result



Sol = Solution()

temperaturesi = [73,74,75,71,69,72,76,73]
resulti = [1,1,4,2,1,1,0,0]

temperaturesii = [30,40,50,60]
resultii = [1,1,1,0]


temperaturesiii = [30,60,90]
resultiii = [1,1,0]

temperaturesiv = [100, 90, 80, 70]
resultiv = [0, 0, 0, 0]




print(Sol.dailyTemperatures(temperaturesi) == resulti)
print(Sol.dailyTemperatures(temperaturesii) == resultii)
print(Sol.dailyTemperatures(temperaturesiii) == resultiii)
print(Sol.dailyTemperatures(temperaturesiv) == resultiv)





class UndergroundSystem:

    def __init__(self):

        # key is customerID. tuple of metro station and check in time are values.
        self.openTravels = {}
        self.routes = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.openTravels[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        checkinName, checkinTime = self.openTravels[id]
        route = checkinName + "-" + stationName
        travelTime = t - checkinTime

        if route not in self.routes:
            self.routes[route] = [travelTime, 1]
        else:
            oldTotal, oldCount = self.routes[route]
            self.routes[route] = [travelTime + oldTotal, oldCount + 1]

    def getAverageTime(self, startStation: str, endStation: str) -> float:

        route = startStation + "-" + endStation
        totalTravelTime, totalCount = self.routes[route]

        return totalTravelTime / totalCount


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)


Sol = UndergroundSystem()

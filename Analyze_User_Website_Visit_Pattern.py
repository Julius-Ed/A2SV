from typing import List


class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:

        zipList = list(zip(timestamp, username, website))
        zipList.sort()

        individualTraffic = {}

        for time, user, site in zipList:
            if user not in individualTraffic:
                individualTraffic[user] = [site]
            else:
                individualTraffic[user].append(site)

        patterns = {}

        for user in individualTraffic:
            traffic = individualTraffic[user]

            for i in range(2, len(traffic)):
                pat = traffic[i-2] + '-' + traffic[i-1] + '-' + traffic[i]
                if pat not in patterns:
                    patterns[pat] = 1
                else:
                    patterns[pat] += 1

        res = max(patterns, key=patterns.get)
        res = res.split('-')
        return res


Sol = Solution()


username = ["joe", "joe", "joe", "james", "james",
            "james", "james", "mary", "mary", "mary"]
timestamp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
website = ["home", "about", "career", "home", "cart",
           "maps", "home", "home", "about", "career"]

print(Sol.mostVisitedPattern(username, timestamp, website))

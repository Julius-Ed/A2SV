from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        # we need at least max(weights) capacity to ship everything.
        # if we were to have sum(weights) capacity we could ship everything in one load.
        l, r = max(weights), sum(weights)

        # binary search through shipping capacity.
        while l < r:
            mid = (l + r) // 2

            load = 0
            daysNeeded = 1

            for weight in weights:
                load += weight

                # if load is greater than our current shipping capacity, we need to start a new ship.
                if load > mid:
                    # first load of the ship will be the weight that did not fit into the old one.
                    load = weight
                    # ships are synonymous to needed days.
                    daysNeeded += 1

            # if we need more days than we have, we need to increase the shipping capacity, thus decreasing numbers of days required.
            if daysNeeded > days:
                l = mid + 1

            # otherwise we can try decreasing shipping capacity.
            else:
                r = mid

        return l


Sol = Solution()

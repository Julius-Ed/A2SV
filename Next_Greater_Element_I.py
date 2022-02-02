
class Solution:
    def nextGreaterElement(self, nums1, nums2):

        stackGreaterNeighbors = []
        neihborDictionary = {}

        result = []

        for num2 in nums2:

            while len(stackGreaterNeighbors) > 0 and stackGreaterNeighbors[-1] < num2:
                neihborDictionary[stackGreaterNeighbors.pop()] = num2

            stackGreaterNeighbors.append(num2)

        for rest in stackGreaterNeighbors:
            neihborDictionary[rest] = -1

        for num1 in nums1:
            result.append(neihborDictionary[num1])

        return result


Sol = Solution()

nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]
# [-1,3,-1]

# nums1 = [2,4]
# nums2 = [1,2,3,4]
# [3,-1]


# nums1 = [4,1,2]
# nums2 = [1,2,3,4]
# [-1, 2, 3]

print(Sol.nextGreaterElement(nums1, nums2))

import heapq


class Solution:
    def kthLargestNumber(self, nums, k) -> str:

        for index in range(len(nums)):
            nums[index] = int(nums[index])

        nums.sort()

        return str(nums[-k])

    def kthLargestNumber2(self, nums, k) -> str:

        min_heap = []

        for num in nums:
            heapq.heappush(min_heap, int(num))

            if len(min_heap) > k:
                heapq.heappop(min_heap)

        return str(min_heap[0])

    def quickSelect(self, nums, k):

        for i in range(len(nums)):
            nums[i] = int(nums[i])

        target_index = len(nums) - k

        left = 0
        right = len(nums) - 1

        pivot_index = left
        pivot = nums[pivot_index]

        first_round = True

        pivot_index = left
        pivot = nums[pivot_index]

        while True:  

            if not first_round:
                pivot_index = left
                pivot = nums[pivot_index]
            
            first_round = False

            while left < right:



                while left < len(nums) and nums[left] <= pivot:
                    left += 1

                while nums[right] > pivot:
                    right -= 1

                if left < right:
                    nums[left], nums[right] = nums[right], nums[left]

                

            nums[right], nums[pivot_index] = nums[pivot_index], nums[right]



            if right == target_index:
                return nums[right]

            if right < target_index:
                # go to RHS
                left = right + 1
                right = len(nums) - 1

            else:
                # go to LHS
                left = 0
                right = target_index

        return nums[right]


Sol = Solution()
# print(Sol.kthLargestNumber(["3", "6", "7", "10"], k=4))
# print(Sol.kthLargestNumber(["2", "21", "12", "1"], k=3))
# print(Sol.kthLargestNumber(["0", "0"], k=2))

# print(Sol.kthLargestNumber2(["3", "6", "7", "10"], k=4))
#print(Sol.kthLargestNumber2(["2", "21", "12", "1"], k=3))
# print(Sol.kthLargestNumber2(["0", "0"], k=2))


# print(Sol.quickSelect([3, 6, 7, 10], k=4))
# print(Sol.quickSelect([2, 21, 12, 1], k=3))
# print(Sol.quickSelect(["0", "0"], k=2))


print(Sol.quickSelect(["2", "21", "12", "1", "10", "0"], 3))


class Solution:
    def targetIndices(self, nums, target):
        
        nums = self.count_sort(nums)
        result = []

        for index in range(len(nums)):
            if nums[index] == target:
                result.append(index)

        return result
    
    def targetIndicesN(self, nums, target):
        
        smaller_count = 0
        equal_count = 0
    
        for num in nums:
            if num < target:
                smaller_count += 1
            if num == target:
                equal_count += 1
        
        result = [x for x in range(smaller_count, equal_count + smaller_count)]

        return result


    def count_sort(self, arr):

        max_element = int(max(arr))
        min_element = int(min(arr))

        range_of_elements = max_element - min_element + 1


        count_arr = [0 for _ in range(range_of_elements)]
        output_arr = [0 for _ in range(len(arr))]


        for i in range(0, len(arr)):
            count_arr[arr[i]-min_element] += 1


        for i in range(1, len(count_arr)):
            count_arr[i] += count_arr[i-1]

        for i in range(len(arr)-1, -1, -1):
            output_arr[count_arr[arr[i] - min_element] - 1] = arr[i]
            count_arr[arr[i] - min_element] -= 1


        for i in range(0, len(arr)):
            arr[i] = output_arr[i]

        return arr


Sol = Solution()

print(Sol.targetIndices([5, 1, 1, 2, 4], 1))
print(Sol.targetIndicesN([5, 1, 1, 2, 4], 1))
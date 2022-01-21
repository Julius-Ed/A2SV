
class Solution:
    def largestNumber(self, nums):
        
        for i in range(len(nums)):
            nums[i] = str(nums[i])

        for _ in nums:
            for index in range(len(nums) - 1):

                option_a = nums[index] + nums[index + 1]
                option_b = nums[index + 1] + nums[index]

                if int(option_a) < int(option_b):
                    nums[index], nums[index + 1] = nums[index + 1], nums[index]
        
        result = ""

        for num in nums:
            result += num
        
        if result[0] == "0":
            return "0"

        return result
    
    def compare(self, a, b):

        option_a = str(a) + str(b)
        option_b = str(b) + str(a)

        if int(option_a) >= int(option_b):
            return True
        else:
            return False


    def merge(self, left, right):
        result = []

        while left and right:
            #if left[0] >= right[0]:
            if self.compare(left[0], right[0]):
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        
        if left:
            result += left
        if right:
            result += right
        
        return result


    def merge_sort(self, list):

        # def base case
        if len(list) <= 1:
            return list
        

        middle = len(list) // 2

        left = list[:middle]
        right = list[middle:]

        # recursive calls

        left_sorted = self.merge_sort(left)
        right_sorted = self.merge_sort(right)


        return self.merge(left_sorted, right_sorted)
    
    def largestNumber2(self, nums):

        results = self.merge_sort(nums)

        result_string = ""

        for result in results:
            result_string += str(result)
        
        return result_string



Sol = Solution()
#print(Sol.largestNumber([3,30,34,5,9]))


print(Sol.largestNumber2([3, 30 , 34, 5 , 9]))
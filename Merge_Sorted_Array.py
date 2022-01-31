from collections import deque
class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        # all of them will iterate backwards.
        nums_one_pointer = m - 1
        nums_two_pointer = n - 1
        cursor = n + m - 1

        while nums_two_pointer >= 0 and nums_one_pointer >= 0:
            if nums2[nums_two_pointer] >= nums1[nums_one_pointer]:
                nums1[cursor] = nums2[nums_two_pointer]
   
                nums_two_pointer -= 1
  
            else:
                nums1[cursor] = nums1[nums_one_pointer]


                nums_one_pointer -= 1
            

            cursor -= 1

        if nums_two_pointer >= 0:
            for i in range(nums_two_pointer + 1):
                nums1[i] = nums2[i]
        

        return nums1



nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [-4, 0, 6]
n = 3


# nums1 = [0]
# m = 0
# nums2 = [1]
# n = 1


Sol = Solution()
print(Sol.merge(nums1, m, nums2, n))

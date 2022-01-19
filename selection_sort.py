"""
Given an unsorted array of size N, use selection sort to sort arr[] in increasing order.
Constraints: 1 ≤ N ≤ 10^3
"""


class Solution: 

    def select(self, arr, i):

        min_index = i
        min_value = arr[i]

        for j in range(i, len(arr)):
            if arr[j] < min_value:
                min_value = arr[j]
                min_index = j
    
        return min_index

    def selectionSort(self, arr,n):
        
        for i in range(n):
            min_index = self.select(arr, i)
            
            arr[min_index], arr[i] = arr[i], arr[min_index]
        
        return arr

Sol = Solution()

print(Sol.selectionSort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 10))

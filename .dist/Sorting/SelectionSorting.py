# import sys
# def selection_sort(given_list):
#     result = []
#     cur_min = given_list[0]
#     cur_ind = 0
#     for j in range(len(given_list)):
#         for i in range(len(given_list)):
#             if cur_min > given_list[i]:
#                 cur_min = given_list[i]
#                 cur_ind = i
#         result.append(cur_min)
#         given_list[cur_ind] = sys.maxsize
#         cur_min = given_list[0]
#         cur_ind = 0
#     return result

#User function Template for python3
import sys
class Solution: 
    def select(self, arr, i):
        # code here 
        cur_min = arr[i]
        min_ind = i
        for a in range(i,len(arr)):
            if cur_min > arr[a]:
                cur_min = arr[a]
                min_ind = a
        arr[i],arr[min_ind] = arr[min_ind],arr[i]
        
        return arr
        
    def selectionSort(self, arr,n):
        #code here
        for j in range(len(arr)):
            arr = self.select(arr, j)
        
        return arr
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends
#User function Template for python3

class Solution:
    #swaps to elemnts of arr
    def swap(self, arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]
        
    #Heapify function to maintain heap property.
    def heapify(self,arr, n, i):
        # code here
        while(True):
            l, r = i*2+1, i*2+2
            
            if max(l, r) < n:
                if arr[i] >= max(arr[l], arr[r]): break
                elif arr[l] > arr[r]:
                    self.swap(arr, i,l)
                    i = l
                else:
                    self.swap(arr, i, r)
                    i = r
            elif l < n:
                if arr[l] > arr[i]:
                    self.swap(arr, i, l)
                    i = l
                else: break
            elif r < n:
                if arr[r] > arr[i]:
                    self.swap(arr, i, r)
                    i = r 
                else: break
            else: break
    
    #Function to build a Heap from array.
    def buildHeap(self,arr,n):
        # code here
        for j in range(len(arr) -2//2, -1, -1):
            self.heapify(arr, n, j)
    
    #Function to sort an array using Heap Sort.    
    def HeapSort(self, arr, n):
        #code here
        self.buildHeap(arr,n)
        for end in range(len(arr) -1, 0, -1):
            self.swap(arr, 0, end)
            self.heapify(arr, end, 0)

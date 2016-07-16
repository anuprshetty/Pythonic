#User function Template for python3
class Solution:
    def merge(self, left, right):
        res = []
        i, j = 0, 0
        while(i < len(left) and j < len(right)):
            if left[i] > right[j]:
                res.append(right[j])
                j += 1
            else:
                res.append(left[i])
                i += 1
        
        res.extend(left[i:])
        res.extend(right[j:])
        
        return res
    
    def mergeSort(self, arr):
        if len(arr) <= 1:
            return arr
        
        mid = len(arr) // 2

        left = self.mergeSort(arr[:mid])
        right = self.mergeSort(arr[mid:])
        return self.merge(left, right)
    
    def sortArr(self, arr, n): 
        #code here
        res = self.mergeSort(arr)
        return res

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        obj = Solution()
        ans = obj.sortArr(arr, n)
        for i in ans:
            print(i,end=" ")
        print()
# } Driver Code Ends
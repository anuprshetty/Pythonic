#User function Template for python3

# Sliding Window Problem

#Function to find a continuous sub-array which adds up to a given number.
class Solution:
    def subArraySum(self,arr, n, s):
        #Write your code here
        cur_sum = arr[0]
        init_i = 0
        if cur_sum == s:
            return [1, 1]
        for cur_i in range(1, n):
            cur_sum += arr[cur_i]
            while cur_sum > s and init_i < cur_i:
                cur_sum -= arr[init_i]
                init_i += 1
            if cur_sum == s:
                return [init_i+1, cur_i+1]
        
        return [-1]
                

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math

def main():
        T=int(input())
        while(T>0):
            
            NS=input().strip().split()
            N=int(NS[0])
            S=int(NS[1])
            
            A=list(map(int,input().split()))
            ob=Solution()
            ans=ob.subArraySum(A, N, S)
            
            for i in ans:
                print(i, end=" ")
                
            print()
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends
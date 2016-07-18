#User function Template for python3

# Not Keeping the order of both Pos and Neg values.
# Approach: 2 pointers problem.
# Time Complexity: O(n)
# Space Complexity: O(1)

# Only keeping the order of Pos values.
# Approach: Traverse from first to last.
# Time Complexity: O(n)
# Space Complexity: O(1)

# -----------------------------------------------------------
# Keeping the order of both Pos and Neg values.
# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def segregateElements(self, arr, n):
        # Your code goes here
        pos, neg = [], []
        for ele in arr:
            if ele < 0:
                neg.append(ele)
            else:
                pos.append(ele)
        
        arr.clear()
        arr.extend(pos)
        arr.extend(neg)
        
        return arr

#{ 
#  Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        ob=Solution()
        ob.segregateElements(a, n)
        print(*a)

        T -= 1


if __name__ == "__main__":
    main()





    
# } Driver Code Ends
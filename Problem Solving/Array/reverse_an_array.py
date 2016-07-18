# Two Pointers Approach

#code
t = int(input())
while(t):
    n = int(input())
    arr = [int(x) for x in input().split()]
    start, end = 0, n-1
    while start < end :
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    
    print(*arr)
    
    t -= 1
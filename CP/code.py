# type: ignore
import sys
sys.stdout = open('CP/output.txt', 'w')
sys.stdin = open('CP/input.txt', 'r') 

#type your code below
n, x = map(int, input().split())
a = list(map(int, input().split()))
ans = 0
a.sort()
i = 1
for i in range(1, n):
    if a[i] + a[i-1] <= x:
        ans+=1
        
    else:
        ans+=1
        
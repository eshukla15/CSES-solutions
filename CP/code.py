# type: ignore
import sys
sys.stdin = open('CP/input.txt', 'r') 
sys.stdout = open('CP/output.txt', 'w')

#type your code here
# t = int(input())
# for _ in range(t):
#     n = int(input())
#     a = list(map(int, input().split()))
    
#     if n <= 2:
#         print(sum(abs(a[i] - a[i-1]) for i in range(1, n)))
#         continue
    
#     max_reduction = -1
#     idx = -1
    
#     # Check removing each element
#     for i in range(n):
#         # Calculate reduction in sum if we remove element at index i
#         if i == 0:
#             # First element: only loses |a[1] - a[0]|
#             reduction = abs(a[1] - a[0])
#         elif i == n - 1:
#             # Last element: only loses |a[n-1] - a[n-2]|
#             reduction = abs(a[n-1] - a[n-2])
#         else:
#             # Middle element: loses |a[i] - a[i-1]| + |a[i+1] - a[i]|
#             # but gains |a[i+1] - a[i-1]|
#             current = abs(a[i] - a[i-1]) + abs(a[i+1] - a[i])
#             after = abs(a[i+1] - a[i-1])
#             reduction = current - after
        
#         if reduction > max_reduction:
#             max_reduction = reduction
#             idx = i
    
#     # Remove the element
#     a.pop(idx)
    
#     # Calculate sum of adjacent differences
#     total = sum(abs(a[i] - a[i-1]) for i in range(1, len(a)))
#     print(total)
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, amount = map(int, input().split())
    c = list(map(int, input().split()))
    cache = {}
    


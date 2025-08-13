# type: ignore
import sys
sys.stdout = open('CP/output.txt', 'w')
sys.stdin = open('CP/input.txt', 'r') 

#type your code below
t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    s1 = (2*b - a) % 3
    s2 = (2*a - b) % 3
    if s1+s2 == 0:
        print("YES")
    else:
        print("NO")
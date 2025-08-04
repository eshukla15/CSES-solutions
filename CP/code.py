# type: ignore
import sys
sys.stdout = open('CP/output.txt', 'w')
sys.stdin = open('CP/input.txt', 'r') 

n = int(input())
s = n * (n+1)
if s % 4 == 0:
    print("YES")
    s = s//4
    s1 = []
    s2 = []
    while n:
        if n <= s:
            s1.append(n)
            s -= n
        else:
            s2.append(n) 
        n-=1
    print(*s1)
    print(*s2)

else:
    print("NO")
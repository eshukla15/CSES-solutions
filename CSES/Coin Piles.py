"""
should be divisible by 3
and if one in 
"""
t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    print("YES" if (a + b) % 3 == 0 and min(a, b) * 2 >= max(a, b) else "NO")


"""
s = n integers sum
s = s1 + s2
assuming s1 = s2
s = 2s1
n integers sum = n(n+1) / 2
s = n(n+1) / 2 = 2s1 or 2s2
s = n(n+1) / 4
=> s should be div by 4 to be in equal sets

sum is n(n+1) / 2
take half of it, must be in one set
keep substracting numbers, like we use to convert binary and decimal logic
"""

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
    print(len(s1))
    print(*s1)
    print(len(s2))
    print(*s2)

else:
    print("NO")


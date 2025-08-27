t = int(input())
a = list(map(int, input().split()))
a.sort()
if a[-1] != t:
    print(t)
else:
    for i in range(1, t):
        if a[i-1] != i:
            print(i)
            break
         

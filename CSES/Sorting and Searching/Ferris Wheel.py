n, x = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
i = 1
while i < n:
    if a[i] + a[i-1] <= x:
        ans+=1
        i+=2
    else:
        ans+=1
        i+=1
print(ans)
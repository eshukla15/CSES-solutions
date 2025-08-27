
n = int(input())
a = list(map(int, input().split()))
a.sort()
ans = 1
for i in range(1, len(a)):
    if a[i] != a[i-1]:
        ans+=1
print(ans)
n, x = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

i = 0
ans = 0
l = 0
r = n - 1
while r >= l:
    if a[l] + a[r] <= x:
        l += 1
        r -= 1
        ans += 1
    else :
        r -= 1
        ans += 1
print(ans)

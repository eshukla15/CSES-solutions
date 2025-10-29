n, m, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort()

pa = 0
pb = 0  # for b
res = 0

while pa < n and pb < m:
    temp = abs(a[pa] - b[pb])
    if temp <= k:
        res += 1
        pa += 1
        pb += 1
    elif a[pa] < b[pb]:
        pa += 1
    else:
        pb += 1
print(res)

import sys
input = sys.stdin.readline

n, q = map(int, input().split())
arr = list(map(int, input().split()))
pref = [arr[0]]
for i in range(1, n):
    pref.append(pref[-1] + arr[i])
res = []
for i in range(q):
    a, b = map(int, input().split())
    if a == b:
        res.append(arr[a-1])
    elif a - 2 >= 0:
        res.append(pref[b-1] - pref[a-2])
    else:
        res.append(pref[b-1])
print('\n'.join(res))
import sys
input = sys.stdin.readline

n, q = map(int, input().split())
arr = list(map(int, input().split()))
pref = [arr[0]]
for i in range(1, n):
    pref.append(pref[-1] + arr[i])

for i in range(q):
    a, b = map(int, input().split())
    if a == b:
        print(arr[a-1])
    elif a - 2 >= 0:
        print(pref[b-1] - pref[a-2])
    else:
        print(pref[b-1])
    
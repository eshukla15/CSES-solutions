n = int(input())
time = []
for _ in range(n):
    i, o = map(int, input().split())
    time.append([i,o])

time.sort(key= lambda x:x[1])

res = 0
curEndTime = -1

for i in range(n):
    if curEndTime <= time[i][0]:
        res += 1
        curEndTime = time[i][1]
print(res)
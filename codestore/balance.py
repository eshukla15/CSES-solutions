n = int(input())
maxrval = float('-inf')
r, c = [-1], [-1]
mat = []

for i in range(n):
    temp = list(map(int, input().split()))

    if sum(temp) >= maxrval:
        if r[0] == -1:
            r[0] = i
        else:
            r.append(i)
    mat.append(temp)

# making array of col sum values
mincval = float('inf')
for r in range(n):
    csum = 0
    for k in range(n):
        csum += mat[k][r]
    
    if csum <= mincval:
        mincval = csum
        if c[0] == -1:
            c[0] = i
        else:
            c.append(i)

r = list(set(r))
c = list(set(c))

if len(r) == 1:
    if r[0] in c:
        print("Balanced")
elif len(c) == 1:
    if c[0] in r:
        print("Balanced")
else:
    print("imbalanced")
print(r, c)





n = int(input())
time = []
cIn = []
cOut = []
for _ in range(n):
    i, o = map(int, input().split())
    cIn.append(i)
    cOut.append(o)
cIn.sort()
cOut.sort()
i = 0
j = 0
maxCustomers = 0
customer = 0
while i < n and j < n:
    if cIn[i] < cOut[j]:
        i += 1
        customer += 1
        maxCustomers = max(maxCustomers, customer)
    else:
        j += 1
        customer -= 1
    
print(maxCustomers)
n = int(input())
o = []
e = []
if n in set([0, 2, 3]):
    print("NO SOLUTION")
else:
    for i in range(1, n+1):
        if i%2:
            o.append(i)
        else:
            e.append(i)
    
    for i in o:
        e.append(i)
    print(*e)

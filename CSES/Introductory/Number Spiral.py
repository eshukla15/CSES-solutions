t = int(input())

for _ in range(t):
    y, x = map(int, input().split())

    maxi = max(x, y)
    square = (maxi - 1) * (maxi - 1)

    if maxi % 2 == 0:
        if x > y:
            print(square + y)
        else:
            print(maxi * maxi - x + 1)
    else:
        if x > y:
            print(maxi * maxi - y + 1)
        else:
            print(square + x)


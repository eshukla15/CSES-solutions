#same approach as last one
#find all pairs

n = int(input())
a = list(map(int, input().split()))

def calc(index, sum1, sum2, arr):
    if index == n:
        return abs(sum1 - sum2)
    
    choose = calc(index+1, sum1+a[index], sum2, arr)

    not_choose = calc(index+1, sum1, sum2+a[index], arr)

    return min(choose, not_choose)

print(calc(0, 0, 0, a))

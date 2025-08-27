n = int(input())
 ########   from , using, to ########
def toh(n, source, helper, target):
    if n == 1:
        print(source, target)
        return
    toh(n-1, source, target, helper)
    print(source, target)
    toh(n-1, helper, source, target)
print(2**n - 1)
toh(n, 1, 2, 3)
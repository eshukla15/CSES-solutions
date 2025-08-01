# type: ignore
import sys
sys.stdout = open('CP/output.txt', 'w')
sys.stdin = open('CP/input.txt', 'r') 

t = int(input())
for _ in range(t):   
    x, y = (map(int, input().split()))

    #first remove the numbers of the square before it
    #then according to parity add the remaining part
    if x > y:
        if x % 2 == 0:
            print((x-1)**2 + x*2 - y)
        else:
            print((x-1)**2 + y)

    else:
        if y % 2 == 0:
            print((y-1)**2 + y - 2*x)
        else:
           print((y-1)**2 + x) 



            


   

    
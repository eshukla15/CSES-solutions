n = int(input())
for i in range(1, n+1):
    total = (i**4 - i**2) // 2    #nC2 for each piece and its reverse
    #here n will be i^2 because i*i board and 2 knights to be chosen
    #each 2x3 block will have 2 
    #each 3x2 block will have 2
    #number of 2x3 and 3x2 in n x n block = (n-1)(n-2) and (n-2)(n-1)
    print(total - 4 * (i-1)*(i-2))
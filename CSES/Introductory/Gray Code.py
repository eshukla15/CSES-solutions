n=int(input())

"""
Idea is to generate recursively.
reverse half part in order to ensure only one bit changes
For n=4
gray_code(4)
 ├─> gray_code(3)
 │     ├─> gray_code(2)
 │     │     ├─> gray_code(1) = ["0","1"]
 │     │     └─> build n=2 = ["00","01","11","10"]
 │     └─> build n=3 = ["000","001","011","010","110","111","101","100"]
 └─> build n=4 = ["0000",...,"1000"]

"""
def gray_code(n):
    # Base case
    if n == 1:
        return ["0", "1"]

    # Recursive call
    prev = gray_code(n - 1)   # a list is returned
    result = []            #  a new one is initialised and prev is used

    # Step 1: Prefix '0' to the first half
    for code in prev:
        result.append("0" + code)

    # Step 2: Prefix '1' to the reversed second half
    for code in reversed(prev):
        result.append("1" + code)

    return result
res = gray_code(n)
for i in res:
    print(i)

#---------------------------------#

"""
Idea is to use the formula for generating gray code from binary numbers
first we ll generate binary numbers from 0 to 2^n -1
since gray code for binary number b is given by b ^ (b>>1) [xor operation with b right shifted by 1]
G(i) = i ^ (i / 2).
To understand this, observe that for any binary number i, 
when you divide it by 2 (or equivalently shift it right by one bit: i >> 1), 
you are essentially moving all the bits to the right. XOR-ing (^) this shifted version with the original number i changes exactly one bit, 
thus satisfying the Gray code property. 
Also, since the sequence starts from 0, and we do this operation for all numbers from 0 to 2^n - 1, 
we ensure no duplicates while also encompassing the entire range.
"""
def g(n):
    return n ^ (n >> 1)

for i in range(2**n):
    print ("{0:0{1}b}".format(g(i),n))
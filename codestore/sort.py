
#find primes
#bring largest at 0 index
#smallest at last
#arrange remaining elements in descending oder



import math
def prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True
print(prime(2))

data = list(map(int, input().split()))

primes = []
nonPrime = []
for i in range(len(data)):
    if prime(data[i]):
        primes.append(data[i])
    else:
        nonPrime.append(data[i])
if len(primes) >= 2:
    primes.sort() # ascending
    #popping because we need to add back
    largestP = primes.pop()    
    smallestP = primes.pop(0)  
    
    remaining = primes + nonPrime
    
    #sort all
    remaining.sort(reverse=True)
    
    res = [largestP] + remaining + [smallestP]
    print(res)

#1prime -> first place
elif len(primes) == 1:
    remaining = nonPrime
    remaining.sort(reverse=True)
    print([primes[0]] + remaining)
    
else:
    #no prime case
    data.sort(reverse=True)
    print(data)
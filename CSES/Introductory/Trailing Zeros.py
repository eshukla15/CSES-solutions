"""
To determine the number of zeros at the end of a factorial, 
recursively divide the number by 5 until the quotient is less than 5, 
and sum the results after applying the greatest integer function.

The greatest integer function (usually denoted by brackets) is the 
rounded down integer of a value. 
For example, [5] = 5, [4.5] = 4, [-4.5] = -5.

For example, the number of trailing zeros in 395! 
is ([395/5]=79) + ([79/5]=15) + ([15/5]=3) = 97.
"""

n = int(input())
c = 0
while n >= 5:
    n = n//5
    c += n
print(c)
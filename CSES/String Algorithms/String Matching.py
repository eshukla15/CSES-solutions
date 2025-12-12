s = input()
t = input()

s1 = len(s)
t1 = len(t)
i = 0
j = i+t1
c = 0
while j <= s1:
   
    if s[i:j] == t:
        c += 1
    i += 1
    j = i + t1
print(c)
# sliding window is a linear time solutionw which wont work for this problem
# O n*m since every partition is also compared inside loop

# KMP algorithm uses O n+m time
# once to form a prefix array 

def prefix(s, t):
    pref = [0] * len(s)
    
    j = 0
    while j < len(t):
        pass
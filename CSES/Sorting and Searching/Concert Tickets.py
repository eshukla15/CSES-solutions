# bisect module is used
# uses binary search properties
# to insert and find index in sorted list
# or maintain a sorted order in Ologn time
# in this question, check if the price can be afforded
# you can remove the element
# check the price in array which is greater than the customers price
# if its the first element, then alas!
# the bisect wont work or any type of sorted list also wont work 
# or here, sortedList cannot be used
# since pip install is needed
# because that may give to nsquare
# we use DSU Nnow

import bisect
n, m = map(int, input().split())
h = list( map(int, input().split()))
t = list( map(int, input().split()))
h.sort()
# DSU parent: parent[i] = largest index ≤ i that is still available
parent = list(range(n))
def find(x):
    if x < 0:
        return -1
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]
#refer to DSU.txt example
for i in t:
    idx = bisect.bisect(h, i) - 1
    # now find the parent
    i = find(idx)   #stores the actual parent or index
    if i == -1:
        print(-1)
    else:
        print(h[i])
        # After using ticket i, the next available is i-1
        parent[i] = find(i - 1)
        
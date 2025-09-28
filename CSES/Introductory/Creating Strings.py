#simple backtracking
#make a used array to check if element is to be used or skipped

s = input()
res = set()
n = len(s)
used = [False] * n
def backtrack(path, used, res):    #a path(list of characters), used array, result
    if len(path) == n:  #base case
        res.add("".join(path))
        return
    
    for i in range(n):
        if used[i]:
            continue

        path.append(s[i])    #use the element
        used[i] = True

        backtrack(path, used, res)   #backtrack furthur

        used[i] = False    #remove the element
        path.pop()

s = sorted(s)
backtrack([], used, res)
res = sorted(list(res))    #sorted for lexicographic order
print(len(res))
for i in res:
    print(i)
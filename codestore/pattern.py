n = input()
size = (2 *n) - 1
for i in range(size):  # if 4 then 7, i.e. repeated from 0-6
    for j in range(size): # same 7*7
        top = i  
        bottom = size-i- 1
        left = j
        right = size-j-1
        dist = min(top, bottom, left, right)
        print(n - dist, end="")
        
    print() #new line


# n = input()
# size = (2 *n) - 1
# for i in range(size):  
#     for j in range(size): 
#         dist = min(i, size-i- 1, j, size-j-1)
#         print(n - dist, end="")
#     print()

n = int(input())
size = 2*n - 1
arr = [[0] * size for _ in range(size)]

start = 0
end = size - 1
value = n

while value > 0:
    for i in range(start, end + 1):
        arr[start][i] = value   #top
        arr[end][i] = value     #bottom
        arr[i][start] = value   #left
        arr[i][end] = value     #right

    start += 1
    end -= 1
    value -= 1

for row in arr:
    print(*row)
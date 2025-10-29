#input of board
board = []
for _ in range(8):
    s = list(input())
    board.append(s)

#creating a copy of board using deep copy
#since shallow copy can affect board
import copy
sub = copy.deepcopy(board)

res = []  #stores all results
diag = set() #r+c
antidiag = set()  #r-c
col = set()  #c

def backtrack(r):   #parameters, each state
    #base case: if last row is reached i.e. (0-7 traversed)
    if r == 8:
        res.append(sub.copy())
        return
    #traverse each col and put queen where possible
    for c in range(8):  
        if c in col or r+c in diag or r-c in antidiag or board[r][c] == "*":
            continue
        
        #put a queen
        board[r][c] == 'Q'
        col.add(c)
        diag.add(r+c)
        antidiag.add(r-c)

        #move furthur in that board
        backtrack(r+1)

        #undo the choice and move furthur
        board[r][c] == "."
        col.remove(c)
        diag.remove(r+c)
        antidiag.remove(r-c)

backtrack(0)
print(len(res))
import sys

def solve():
    # Fast I/O
    input = sys.stdin.read().split()
    if not input:
        return
    
    n = int(input[0])
    k = int(input[1])
    nums = input[2:] # Reading everything at once is often faster
    
    hm = {}
    
    for i in range(n):
        val = int(nums[i])
        complement = k - val
        
        if complement in hm:
            # Output 1-based indexing
            print(f"{hm[complement] + 1} {i + 1}")
            return
        
        hm[val] = i
        
    print("IMPOSSIBLE")

if __name__ == "__main__":
    solve()
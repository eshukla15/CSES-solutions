# type: ignore
import sys
sys.stdin = open('CP/input.txt', 'r') 
sys.stdout = open('CP/output.txt', 'w')

# #t = int(input())
# #s = input()
# # l = list(map(int, input().split()))
# # map(int, input().split())

# # def can_sort(n, a):
# #     """
# #     Determine if permutation a can be sorted using swaps between i and 2i.
    
# #     The key insight: p form a forest of trees where i connects to 2i.
# #     A permutation is sortable iff each tree contains exactly the values that
# #     should be in those positions in the sorted array.
# #     """
# #     # For each position, find which tree it belongs to by going up to the root
# #     def get_root(pos):
# #         while pos > 1 and pos % 2 == 0:
# #             pos //= 2
# #         return pos
    
# #     # Group positions by their root (tree component)
# #     from collections import defaultdict
# #     trees = defaultdict(list)
    
# #     for pos in range(1, n + 1):
# #         root = get_root(pos)
# #         trees[root].append(pos)
    
# #     # For each tree, check if the values at those positions
# #     # match the values that should be there in sorted order
# #     for root, positions in trees.items():
# #         positions.sort()
        
# #         # Get values currently at these positions
# #         current_values = sorted([a[p - 1] for p in positions])
        
# #         # Get values that should be at these positions (in sorted array)
# #         target_values = sorted(positions)
        
# #         # Check if they match
# #         if current_values != target_values:
# #             return "NO"
    
# #     return "YES"


# # def main():
# #     t = int(input()) 
# #     for _ in range(t):
# #         n = int(input())
# #         a = list(map(int, input().split()))
# #         print(can_sort(n, a))

# # if __name__ == "__main__":
# #     main()

# def solve():
#     adj = {1: {2, 3, 4, 5},2:{1,3, 4, 6},3:{1, 2, 5, 6},4:{1, 2, 5, 6},5: {1, 3, 4, 6},6: {2, 3, 4, 5}}
#     n = int(input())
#     a = list(map(int, input().split()))
#     if n == 1:
#         print(0)
#         return
#     dp = [[float('inf')]*7 for _ in range(n)]
#     for v in range(1,7):
#         dp[0][v] = 0 if a[0] == v else 1
#     for i in range(1, n):
#         for curr in range(1, 7):
#             c = 0 if a[i] == curr else 1
#             for prev in range(1, 7):
#                 if prev in adj[curr]:
#                     dp[i][curr] = min(dp[i][curr], dp[i-1][prev] + c)
#     res = min(dp[n-1][1:])
#     print(res)
# t = int(input())
# for _ in range(t):
#     solve()

n = int(input())

size = (2 *n) - 1
for i in range(size):  # if 4 then 7, i.e. repeated from 0-6
    for j in range(size): # same 7*7
        top = i  
        bottom = size-i- 1
        left = j
        right = size-j-1
        dist = min(top, bottom, left, right)
        print(n - dist, end="  ")
        
    print() #new line

    






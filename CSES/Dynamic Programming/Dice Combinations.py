# from functools import lru_cache
# n = int(input())
# c = 0
# MOD = 10**9 + 7
# @lru_cache
# def dp(target):
#     if target == 0:
#         return 1
#     if target < 0:
#         return 0
#     total = 0
#     for i in range(1, 7):
#         total += dp(target - i)
#     return total % MOD
# print(dp(n))

# -!!! If recursion depth depends on input size → DON’T USE RECURSION !!! --

# import sys
# n = int(sys.stdin.readline())
# c = 0
# MOD = 10**9 + 7
# dp = [0] * (n+1)
# dp[0] = 1
# for i in range(1, n + 1):
#     for j in range(1, 7):
#         if i - j >= 0:
#             dp[i] = (dp[i] + dp[i - j]) % MOD

# print(dp[n])

# OPTIMIZED with window sum rolling
import sys

n = int(sys.stdin.readline())
MOD = 10**9 + 7

dp = [0] * (n + 1)
dp[0] = 1
# since we need dp[i] = dp[i-1] + dp[i-2] + ... + dp[i-6]
window = 0

for i in range(1, n + 1):
    window = (window + dp[i - 1]) % MOD
    #You cannot reach i from i-7 with one dice throw.
    if i - 7 >= 0:
        window = (window - dp[i - 7]) % MOD     #take only previous 6 choices
    dp[i] = window

print(dp[n])

#dp problem with optimization of rolling sum window
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

import sys

n = int(sys.stdin.readline())
MOD = 10**9 + 7

dp = [0] * (n + 1)
dp[0] = 1

window = 0

for i in range(1, n + 1):
    window = (window + dp[i - 1]) % MOD
    if i - 7 >= 0:
        window = (window - dp[i - 7]) % MOD
    dp[i] = window

print(dp[n])
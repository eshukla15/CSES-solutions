# type: ignore
import sys
sys.stdin = open('CP/input.txt', 'r') 
sys.stdout = open('CP/output.txt', 'w')

#type your code here
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
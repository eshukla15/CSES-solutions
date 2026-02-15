x = 6
# Use bit operations when possible
x // 2  # can be x >> 1
x * 2   # can be x << 1
x % 2   # can be x & 1

# Use divmod for both quotient and remainder
q, r = divmod(a, b)  # Better than q = a//b; r = a%b

matrix = [list(map(int, input().split())) for _ in range(n)]
arr = [int(input()) for _ in range(n)]

import sys
sys.stdout.write('\n'.join(map(str, results)) + '\n')


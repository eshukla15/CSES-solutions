x = 6
# Use bit operations when possible
x // 2  # can be x >> 1
x * 2   # can be x << 1
x % 2   # can be x & 1

# Use divmod for both quotient and remainder
q, r = divmod(a, b)  # Better than q = a//b; r = a%b

matrix = [list(map(int, input().split())) for _ in range(n)]
arr = [int(input()) for _ in range(n)]


#output in a line
import sys
sys.stdout.write('\n'.join(map(str, results)) + '\n')


# Method 1: join (good)
print('\n'.join(results))

# Method 2: sys.stdout.write (slightly faster)
sys.stdout.write('\n'.join(results) + '\n')

# Method 3: write each line (still better than print loop)
for r in results:
    sys.stdout.write(r + '\n')

    
#fast input
import sys
input = sys.stdin.readline

n, q = map(int, input().split())
arr = list(map(int, input().split()))

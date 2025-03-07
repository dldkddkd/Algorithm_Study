import math

T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    if n > m:
        print(0)
    else:
        print(math.comb(m, n))
from collections import deque


def is_prime(num):
    if num == 2 or num == 3:
        return True

    for n in range(2, int(num**0.5) + 1):
        if num % n == 0:
            return False
    return True

def is_valid(num1, num2):
    num1 = list(str(num1))
    num2 = list(str(num2))
    count = 0
    for i in range(4):
        if num1[i] != num2[i]:
            count += 1
    return count == 1

N = int(input())
for n in range(N):
    a, b = map(int, input().split())

    primes = []
    for i in range(1000, 10000):
        if is_prime(i):
            primes.append(i)

    q = deque([(a, b, 0)])
    visited = set()
    visited.add(a)
    count = 0
    flag = False
    while q:
        a, b, count = q.popleft()
        if a == b:
            flag = True
            break
        for prime in primes:
            if prime not in visited and is_valid(a, prime):
                visited.add(prime)
                q.append((prime, b, count + 1))

    if flag:
        print(count)
    else:
        print("Impossible")
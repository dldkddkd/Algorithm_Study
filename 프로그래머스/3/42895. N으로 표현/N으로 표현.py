def solution(N, number):
    if N == number:
        return 1

    S = [set() for _ in range(9)]
    for i in range(1, 9):
        S[i].add(int(str(N) * i))
        
        for j in range(1, i):
            for x in S[j]:
                for y in S[i-j]:
                    S[i].add(x + y)
                    S[i].add(x - y)
                    S[i].add(x * y)
                    if y != 0:
                        S[i].add(x // y)
        
        if number in S[i]:
            return i

    return -1

print(solution(2, 11))  # 4
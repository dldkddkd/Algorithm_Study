def solution():
    cnt = 0
    N = int(input())

    P = list(map(int, input().split()))
    S = list(map(int, input().split()))

    arr = list(P)  
    original = list(P) 

    def check(arr):
        for i in range(N):
            if arr[i] % 3 != i % 3:
                return False
        return True

    if check(arr):  
        return 0

    while True:
        cnt += 1
        new_arr = [None] * N
        for i in range(N):
            new_arr[S[i]] = arr[i]
        arr = new_arr

        if check(arr): 
            return cnt
        if arr == original:  
            return -1

print(solution())

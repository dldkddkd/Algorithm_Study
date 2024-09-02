def foo(N):
    answer = 0
    
    array = list(map(int, input().split()))
    for item in array:
        cnt = 0
        for i in range(item, 0, -1):
            if item % i == 0:
                cnt += 1
        if cnt == 2:
            answer += 1

    return answer

N = int(input())    
print(foo(N))
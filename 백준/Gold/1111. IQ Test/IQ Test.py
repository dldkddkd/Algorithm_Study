def solution():
    N = int(input())    
    arr = list(map(int, input().split()))

    if N == 1:
        return "A"
    elif N == 2:
        return arr[0] if arr[0] == arr[1] else "A"

    # a, b 값 계산
    if arr[1] == arr[0]:  
        a, b = 1, 0
    else:
        a = (arr[2] - arr[1]) / (arr[1] - arr[0])
        b = arr[1] - a * arr[0]

        # 정수가 아닌 경우 "B" 반환
        if not a.is_integer() or not b.is_integer():
            return "B"

        a, b = int(a), int(b)

    # 모든 숫자가 동일한 규칙을 따르는지 확인
    for i in range(1, N):
        if arr[i] != a * arr[i - 1] + b:
            return "B"

    # 다음 숫자 계산
    return a * arr[-1] + b

print(solution())

#양의 정수 n이 주어졌을 때, 이를 이진수로 나타냈을 때 1의 위치를 모두 찾는 프로그램을 작성하시오. 
#최하위 비트(least significant bit, lsb)의 위치는 0이다.

T = int(input())

for t in range(T):
    lst = []
    n = int(input())
    while (n > 0):
        lst.append(n % 2)
        n = int(n / 2)

    for idx in range(len(lst)):
        if lst[idx] == 1:
            print(idx, end=' ')
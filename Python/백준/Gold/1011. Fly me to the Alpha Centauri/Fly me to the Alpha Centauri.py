N = int(input())

for n in range(N):
    s, e = map(int, input().split())
    dist = e - s

    cnt = 0
    speed = 1
    while dist > speed * 2:
        dist -= speed * 2
        cnt += 2
        speed += 1

    if dist > speed:
        cnt += 2
    else:
        cnt += 1

    print(cnt)

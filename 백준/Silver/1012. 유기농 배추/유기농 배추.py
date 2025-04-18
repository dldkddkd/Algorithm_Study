from collections import deque

def foo(m, n, farm):
    visit = [[False] * m for _ in range(n)]  # 방문 여부 체크 배열
    count = 0
    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]

    for i in range(n):
        for j in range(m):
            if farm[i][j] == 1 and not visit[i][j]:  # 배추가 있고 방문 안 했으면 BFS 시작
                count += 1  # 새로운 배추 군집 발견
                queue = deque([(i, j)])
                visit[i][j] = True  # 방문 체크

                while queue:
                    x, y = queue.popleft()
                
                    for v in range(4):
                        tx = x + dx[v]
                        ty = y + dy[v]
                        if 0 <= tx < n and 0 <= ty < m and farm[tx][ty] == 1 and not visit[tx][ty]:
                            queue.append((tx, ty))
                            visit[tx][ty] = True  # 방문 체크

    return count

T = int(input())

for _ in range(T):
    m, n, k = map(int, input().split())
    farm = [[0] * m for _ in range(n)]  # 농장 초기화
    for _ in range(k):
        x, y = map(int, input().split())
        farm[y][x] = 1  # 좌표 반영
        
    print(foo(m, n, farm))

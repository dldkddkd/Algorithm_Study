from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]
    
    visit = [[1] * 101 for _ in range(101)]
    queue = deque([(characterX * 2, characterY * 2, 0)])
    
    for x1, y1, x2, y2 in rectangle:
        for tx in range(x1 * 2, x2 * 2 + 1):
            for ty in range(y1 * 2, y2 * 2 + 1):
                visit[tx][ty] = 0
            
    for x1, y1, x2, y2 in rectangle:
        for tx in range(x1 * 2 + 1, x2 * 2):
            for ty in range(y1 * 2 + 1, y2 * 2):
                visit[tx][ty] = 1

    # for i in range(20, -1, -1):
    #     for j in range(20):
    #         if visit[j][i] == 0:
    #             print(visit[j][i], end=" ")
    #         else:
    #             print(".", end=" ")
    #     print()
    
    while queue:
        x, y, count = queue.popleft()
        visit[x][y] = 1
        if x == itemX * 2 and y == itemY * 2:
            return int(count / 2)
        
        for i in range(4):
            ix = x + dx[i]
            iy = y + dy[i]
            
            if ix <= 0 or ix > 100 or iy <= 0 or iy > 100 or visit[ix][iy] == 1:
                continue
            queue.append((ix, iy, count + 1))    
                
    
    return 0

# rectangle = [[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]]
# print(solution(rectangle, characterX=1, characterY=3, itemX=7, itemY=8))
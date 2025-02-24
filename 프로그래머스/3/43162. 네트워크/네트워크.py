from collections import defaultdict, deque

def solution(n, computers):
    visited = [False] * n
    network_count = 0

    def bfs(start):
        queue = deque([start])
        visited[start] = True
        while queue:
            node = queue.popleft()
            for i in range(n):
                if computers[node][i] == 1 and not visited[i]:
                    visited[i] = True
                    queue.append(i)

    for i in range(n):    
        if not visited[i]:
            bfs(i)
            network_count += 1

    return network_count

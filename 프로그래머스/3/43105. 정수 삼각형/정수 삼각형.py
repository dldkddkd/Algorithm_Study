def solution(triangle):
    answer = 0
    height = len(triangle)
    
    for h in range(1, height):
        for i in range(len(triangle[h])):
            if i == 0:
                triangle[h][i] += triangle[h - 1][i]
            elif i == len(triangle[h]) - 1:
                triangle[h][i] += triangle[h - 1][i - 1]
            else:
                triangle[h][i] = max(triangle[h - 1][i], triangle[h - 1][i - 1]) + triangle[h][i]
    
    answer = max(triangle[height - 1])

    return answer

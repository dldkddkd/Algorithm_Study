def solution(arr):    
    length = (len(arr) + 1) // 2
    
    mx = [[0] * length for _ in range(length)]
    mn = [[0] * length for _ in range(length)]
    for i in range(length):
        mx[i][i] = mn[i][i] = int(arr[i * 2])
        
    for l in range(2, length + 1):
        for i in range(length - l + 1):
            j = i + l - 1
            mx[i][j] = float('-inf')
            mn[i][j] = float('inf')
            
            for k in range(i, j):
                if arr[k * 2 + 1] == "+":
                    mx[i][j] = max(mx[i][j], mx[i][k] + mx[k+1][j])
                    mn[i][j] = min(mn[i][j], mn[i][k] + mn[k+1][j])
                else:
                    mx[i][j] = max(mx[i][j], mx[i][k] - mn[k+1][j])
                    mn[i][j] = min(mn[i][j], mn[i][k] - mx[k+1][j])
    
    return mx[0][length-1]
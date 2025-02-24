def dfs(numbers, target, index, cur, wrapper):
    if index == len(numbers):
        if cur == target:
            wrapper[0] += 1
        return

    dfs(numbers, target, index + 1, cur + numbers[index], wrapper)
    dfs(numbers, target, index + 1, cur - numbers[index], wrapper)

def solution(numbers, target):    
    answer = [0]
    dfs(numbers, target, 0, 0, answer)
    return answer[0]
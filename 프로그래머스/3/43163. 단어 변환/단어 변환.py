from collections import deque

def canChange(word1, word2):
    count = sum([1 for a, b in zip(word1, word2) if a != b])  
    return count == 1

def solution(begin, target, words):    
    if target not in words:
        return 0
    
    queue = deque([(begin, 0)])
    visited = set()

    while queue:
        cur, count = queue.popleft()
        if cur == target:
            return count

        for word in words:
            if word not in visited and canChange(cur, word):
                visited.add(word)
                queue.append((word, count + 1))
                   
    return 0
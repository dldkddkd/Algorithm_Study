# 1 2 2 3 3 3 4 4 4 4 5

array = [i for i in range(1, 46) for j in range(1, i+1)]

(A, B) = map(int, input().split())
total = 0

for x in range(A - 1, B):
    total += array[x]
    
print(total)
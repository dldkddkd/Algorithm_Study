N, M = map(int, input().split())
array = [0 for _ in range(N)]
lst = []
cnt = 1
for i in range(M):
    l, r = map(int, input().split())
    lst.append((l, r))
    for j in range(l - 1, r):
        array[j] = cnt
    cnt += 1
array = list(set(array))
if array.__contains__(0):
    length = len(array) - 1
else:
    length = len(array)
print(2**length)

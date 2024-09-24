arrs = []

for _ in range(5):
    word = input()
    arrs.append(word)

length = max([len(word) for word in arrs])

for i in range(length):
    for word in arrs:
        if i < len(word): 
            print(word[i], end='')


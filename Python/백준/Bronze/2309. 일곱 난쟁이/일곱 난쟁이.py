def foo(lst: list):
    for i in range(9):
        lst.append(int(input()))

    lst.sort()
    diff = sum(lst) - 100
    for i in range(9):
        for j in range(9):
            if diff == lst[i] + lst[j]:
                item1 = lst[i]
                item2 = lst[j]
                lst.remove(item1)
                lst.remove(item2)
                return lst
            
lst = []
lst = foo(lst)
for item in lst:
    print(item)
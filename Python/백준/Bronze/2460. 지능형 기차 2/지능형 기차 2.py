total = 0
lst = []
for i in range(10):
    (_out, _in) = map(int, input().split())
    total -= _out
    total += _in
    lst.append(total)
    
print(max(lst))
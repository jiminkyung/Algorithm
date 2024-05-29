ret = float("-inf")
place = ()

lst = []

for _ in range(9):
    row = list(map(int, input().split()))
    lst.append(row)

for i in range(9):
    for k in range(9):
        ret = max(ret, lst[i][k])
        if ret == lst[i][k]:
            place = (i+1, k+1)

print(ret)
print(*place, sep=" ")
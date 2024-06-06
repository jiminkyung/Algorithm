# 메모리: 31120KB / 시간: 52ms

M, N = int(input()), int(input())

ret = []
for i in range(M, N+1):
    if i < 2:
        continue

    is_True = True

    for k in range(2, int(i**0.5)+1):
        if i % k == 0:
            is_True = False
            break
    
    if is_True:
        ret.append(i)

if ret:
    print(sum(ret))
    print(min(ret))
else:
    print(-1)


# 최대한 단순하게 해야 시간이 덜 걸리는듯. -> 60ms ㅋㅋㅋ
M, N = int(input()), int(input())

ret = 0
min_ret = float("inf")

for i in range(M, N+1):
    if i < 2:
        continue

    is_True = True

    for k in range(2, int(i**0.5)+1):
        if i % k == 0:
            is_True = False
            break
    
    if is_True:
        ret += i
        min_ret = min(min_ret, i)

if ret:
    print(ret)
    print(min_ret)
else:
    print(-1)
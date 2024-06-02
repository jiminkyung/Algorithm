# while-else문을 사용해본 문제.

N = int(input())

ret = 0
while N >= 0:
    if N % 5 == 0:
        ret += N // 5
        print(ret)
        break
    N -= 3
    ret += 1
else:
    print(-1)
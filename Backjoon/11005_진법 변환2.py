# 31120KB / 40ms

N, B = map(int, input().split())

ret = ""
while N > 0:
    tmp = N % B
    if int(tmp) >= 10:
        tmp = chr(tmp + ord("A") - 10)
    ret = str(tmp) + ret
    N //= B

print(ret)
# 문제집 - 0x12강 - 수학


# 문제: https://www.acmicpc.net/problem/2089
# 메모리: 32412KB / 시간: 32ms
N = int(input())
ret = ""

if N == 0:
    print(0)
else:
    while N != 0:
        # N을 -2로 나눈 나머지가 0이 아닐경우 몫을 추가로 1 더해줌
        if N % -2:
            ret = "1" + ret
            N = N // -2 + 1
        else:
            ret = "0" + ret
            N //= -2
    print(ret)
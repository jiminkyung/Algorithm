# 문제집 - 0x12강 - 수학


# 문제: https://www.acmicpc.net/problem/1292
# 메모리: 32412KB / 시간: 36ms
A, B = map(int, input().split())
seq = [0] * (B+1)

cnt = 0
num = 1

for i in range(1, B+1):
    seq[i] = num
    cnt += 1

    if cnt == num:
        num += 1
        cnt = 0

print(sum(seq[A:]))
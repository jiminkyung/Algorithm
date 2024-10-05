# 문제집 - 대학생 기본반


# 문제: https://www.acmicpc.net/problem/1110
# 메모리: 31252KB / 시간: 40ms
N = int(input())

if N == 0:
    print(1)
else:
    cnt = 0
    curr = N

    while True:
        tmp = curr
        if curr < 10:
            tmp = curr * 10
        t1, t2 = str(tmp)
        tmp = int(t1) + int(t2)
        curr = int(str(curr % 10) + str(tmp % 10))
        cnt += 1
        if curr == N:
            break
    print(cnt)


# 메모리, 시간 모두 효율적인 코드. 단순 계산으로 구하는 방법.
# a = 26 // 10 = 2, b = 26 % 10 = 6
# c = 60 + (2 + 6) % 10 = 68
N = int(input())
a = N//10
b = N%10
i=0

while True:
    c = b*10 + (a+b)%10
    a = c//10
    b = c%10
    i+=1
    if c==N:
        break
    else:
        continue
print(i)
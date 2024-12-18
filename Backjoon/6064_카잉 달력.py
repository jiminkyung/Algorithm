# 문제집 - 0x12강 - 수학


# 문제: https://www.acmicpc.net/problem/6064

# K년을 카잉 달력으로 표현하면 (K % M) : (K % N) 이 된다.
# 단, K == M 와 같이 K가 M이나 N과 같은 값일 경우 위의 식에 대입하면 0 : 0 이 반환되지만, 실제로는 M : N 으로 표현해야한다.
# => M, N = 10, 12 일때 10년을 표현하면 10 : 10, 11년은 1 : 11 이 된다.

# 메모리: 32544KB / 시간: 4448ms
from sys import stdin


input = stdin.readline

T = int(input())

for _ in range(T):
    M, N, x, y = map(int, input().split())

    k = x
    while k <= M * N:
        # k % M == x 와 같이 작성하면 k == M 일때를 처리하지 못함.
        if (k - x) % M == 0 and (k - y) % N == 0:
            print(k)
            break

        k += M
    else:
        print(-1)
# 문제집 - 0x12강 - 수학


# 문제: https://www.acmicpc.net/problem/2960

# 일반적인 에라토스테네스의 체 문제가 아님.
# 지우는 순서를 체크해야하므로 N의 제곱근까지가 아닌 N까지 순회해야한다.

# 메모리: 32412KB / 시간: 36ms
from sys import stdin


input = stdin.readline

N, K = map(int, input().split())

def checking():
    dp = [True] * (N+1)
    dp[0] = dp[1] = False
    cnt = 0

    for i in range(2, N+1):
        if dp[i]:
            cnt += 1
            if cnt == K:
                return i
            for j in range(i*i, N+1, i):
                # 앞에서 지워지지 않은 수일때만 체크
                if dp[j]:
                    dp[j] = False
                    cnt += 1
                    if cnt == K:
                        return j


print(checking())
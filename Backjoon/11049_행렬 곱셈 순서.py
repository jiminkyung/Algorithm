# 동적 계획법 2

"""
크기가 NxM인 행렬 A와 크기가 MxK인 B를 곱할때 필요한 곱셈연산의 수는 NxMxK 이다.

파일 합치기와 비슷함.
ABC가 주어졌을때, (AB)C or A(BC). 이런식으로 체크해야한다.
"""

# PyPy3로 통과한 코드...
from sys import stdin


input = stdin.readline

n = int(input())  # 행렬의 개수
matrices = [list(map(int, input().split())) for _ in range(n)]  # 각 행렬의 크기

# DP 테이블 초기화
dp = [[0] * n for _ in range(n)]

# 부분 문제 해결
for diagonal in range(1, n):  # 대각선 방향으로 진행
    for i in range(n - diagonal):
        j = i + diagonal
        dp[i][j] = float("inf")  # 초기값을 무한대로 설정
        for k in range(i, j):
            cost = dp[i][k] + dp[k+1][j] + matrices[i][0] * matrices[k][1] * matrices[j][1]
            dp[i][j] = min(dp[i][j], cost)

# 결과 출력
print(dp[0][n-1])


# Python3로 통과한 코드 중 제일 효율적인 코드.
import sys
input = sys.stdin.readline

def main():
    for c in range(1, N):   # c: 행렬 개수
        for s in range(N-c):    # s: 시작 인덱스
            t0, e = INF, s+c    # t0: s~e 번째 행렬의 곱셈 연산 수 초기값, e: 마지막 인덱스
            i, j = dp[s][s:e], dp[e][s+1:e+1]
            k, ns = num[s]*num[e+1], num[s+1:e+1]
            for m in range(e-s):   # m: 중간 인덱스
                if t0 > (t:=i[m] + k*ns[m] + j[m]):
                    t0 = t
            dp[s][e] = dp[e][s] = t0
    print(dp[0][N-1])

if __name__ == "__main__":
    INF = 2**31
    N = int(input())
    f = lambda: tuple(map(int, input().split()))
    num = [*f()] + [f()[1] for _ in range(N-1)]
    dp = [[0]*N for _ in range(N)]
    main()
# 다이나믹 프로그래밍
# 비트마스킹


# 문제: https://www.acmicpc.net/problem/1176

# DP, 백트래킹, permutations로 순열 생성 등등...
# 🗝️모두 사용해봤지만 통과되는건 DP + 비트마스킹 요놈뿐. (다른 유형은 TLE)
# 다시 풀어봐야할 문제다. DP!!!

# 메모리: 58560KB / 시간: 1240ms
from sys import stdin


input = stdin.readline

def main():
    N, K = map(int, input().split())
    heights = [int(input()) for _ in range(N)]

    # dp[mask][idx]: 서 있는 학생들의 상태가 mask일때, 마지막에 서있는 학생의 인덱스 idx
    dp = [[0] * N for _ in range(1 << N)]
    for i in range(N):  # 한명씩 서있을때를 먼저 처리해줌
        dp[1 << i][i] = 1
    
    # 1. 최소한 한명은 선택된 상태부터 모두 선택된 상태까지 탐색
    for mask in range(1, 1 << N):
        # 2. 마지막 학생 찾기
        for last in range(N):
            if not (mask & (1 << last)):  # mask에 포함되지 않았다면 패스
                continue
            # 3. 다음에 세울 학생 정하기
            for nxt in range(N):
                if mask & (1 << nxt):  # 이미 서있는 학생이라면 패스
                    continue
                if abs(heights[last] - heights[nxt]) > K:  # 키 차이가 K 초과라면 dp 업데이트
                    dp[mask | (1 << nxt)][nxt] += dp[mask][last]  # 새로운 학생이 마지막으로 섰을때의 dp값 += 서기 전의 dp값
    
    ret = 0
    full = (1 << N) - 1
    # 4. 조건에 맞춰 모두 서있는경우를 취합
    for i in range(N):
        ret += dp[full][i]
    
    print(ret)


main()
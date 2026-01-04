# 다이나믹 프로그래밍
# 비트마스킹
# 비트필드를 이용한 다이나믹 프로그래밍


# 문제: https://www.acmicpc.net/problem/1029

# DP는 해도해도 헷갈린다... DFS로도 풀어봤으나 여전히 헷갈림.
# 나중에 다시 풀어봐야할 문제.

# 1) DP + 비트마스킹 풀이 (bottom-up)
# 메모리: 38552KB / 시간: 304ms
from sys import stdin


input = stdin.readline
INF = int(1e9)

def main():
    N = int(input())
    cost = [list(map(int, input().rstrip())) for _ in range(N)]

    # dp[mask][last]: 교환 상태가 mask이고, 마지막 사람이 last일때의 최소 가격
    dp = [[INF] * N for _ in range(1 << N)]
    dp[1 << 0][0] = 0  # 1번 아티스트는 0을 주고 구매

    for mask in range(1 << N):
        for last in range(N):
            if dp[mask][last] == INF:
                continue
            # last 다음으로 교환할 사람 선정
            for nxt in range(N):
                if mask & (1 << nxt):
                    continue

                # 현재까지의 최소 금액이 last-nxt 간 거래 금액보다 같거나 작으면 교환 가능.
                if dp[mask][last] <= cost[last][nxt]:
                    new_mask = mask | (1 << nxt)
                    dp[new_mask][nxt] = min(dp[new_mask][nxt], cost[last][nxt])
    
    ret = 0

    for mask in range(1 << N):
        for last in range(N):
            if dp[mask][last] != INF:
                ret = max(ret, bin(mask).count("1"))
    
    print(ret)


main()


# 2) DP + 비트마스킹에 DFS를 적용한 풀이 (top-down)
# -> 일반적인 DFS + 메모이제이션 풀이와는 다름.
# 메모리: 48796KB / 시간: 456ms
def main():
    N = int(input())
    cost = [list(map(int, input().rstrip())) for _ in range(N)]

    memo = {}  # 메모이제이션처럼 보이지만 사실상 DP 테이블임.

    def dfs(mask: int, last: int, price: int) -> int:
        # memo[(mask, last)]: 교환 상태가 mask고, 마지막 사람이 last일때의 최저 교환 가격
        # 만약 현재 가격 price가 memo의 가격보다 크거나 같다면 더 볼 필요 없음. 바로 0 리턴.
        if (mask, last) in memo and memo[(mask, last)] <= price:
            return 0
        
        memo[(mask, last)] = price

        best = 1  # 최대 소유 인원

        for nxt in range(N):
            if mask & (1 << nxt):
                continue

            if price <= cost[last][nxt]:
                # max(현재까지의 best, 지금 선택한 사람과 이 사람으로부터 이어나갈 수 있는 소유 인원)
                best = max(best, 1 + dfs(mask | (1 << nxt), nxt, cost[last][nxt]))

        return best
    
    
    print(dfs(1 << 0, 0, 0))


main()
# 최소 신장 트리


# 문제: https://www.acmicpc.net/problem/15681 (트리, 그래프에대한 설명도 존재)
# 메모리: 67308KB / 시간: 372ms
import sys


input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, R, Q = map(int, input().split())
tree = [[] for _ in range(N+1)]
dp = [0] * (N+1)

def counting(dp, curr):
    # 자신도 자신을 루트로 하는 서브트리에 포함되므로 0이 아닌 1에서 시작한다.
    dp[curr] = 1
    for node in tree[curr]:
        if dp[node] == 0:
            counting(dp, node)
            dp[curr] += dp[node]

for _ in range(N-1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

counting(dp, R)

for _ in range(Q):
    print(dp[int(input())])
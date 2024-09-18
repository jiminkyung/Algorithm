# 트리에서의 동적 계획법


# 문제: https://www.acmicpc.net/problem/1949
# 🚨 DP 구조상 자연스럽게 인접한 '우수 마을'이 없도록 선택되기 때문에 3번 조건을 따로 고려할 필요가 없다.

# 메모리: 35452KB / 시간: 56ms
import sys


input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def dfs(node, parent):
    dp[node][0] = 0
    dp[node][1] = people[node]

    for child in tree[node]:
        if child != parent:
            dfs(child, node)
            dp[node][0] += max(dp[child][0], dp[child][1])
            dp[node][1] += dp[child][0]

N = int(input())
people = [0] + list(map(int, input().split()))
tree = [[] for _ in range(N+1)]

for _ in range(N-1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

dp = [[0, 0] for _ in range(N+1)]
dfs(1, 0)  # 1번 노드를 루트로 가정

print(max(dp[1][0], dp[1][1]))
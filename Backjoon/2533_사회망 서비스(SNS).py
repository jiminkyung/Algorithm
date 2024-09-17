# 트리에서의 동적 계획법


# 문제: https://www.acmicpc.net/problem/2533
# 메모리: 311372KB / 시간: 5000ms
import sys


input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(node, parent):
    dp[node][1] = 1
    
    for child in tree[node]:
        if child != parent:
            dfs(child, node)
            dp[node][1] += min(dp[child][1], dp[child][0])
            dp[node][0] += dp[child][1]

N = int(input())

tree = [[] for _ in range(N+1)]
for _ in range(N-1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

dp = [[0, 0] for _ in range(N+1)]

dfs(1, 0)

print(min(dp[1][1], dp[1][0]))


# 실행시간 2364ms인 코드. bottom-up 방식으로 리프노드에서부터 체크한다.
"""
1. 리프 노드부터 시작하여 트리를 상향식으로 처리.
2. 현재 노드가 얼리 어답터가 아니면, 그 부모를 얼리 어답터로 만든다.
3. 현재 노드가 얼리 어답터면, 부모는 얼리 어답터가 될 수도 있고 아닐 수도 있음.
4. 노드의 모든 자식이 처리되면 (req[v] == 1), 그 노드를 처리한다.

- req[n]: 노드 n의 아직 처리되지 않은 이웃 노드의 수
- early: 노드가 얼리어답터인지 체크하는 리스트
"""
from sys import stdin
def main():
    input = stdin.readline
    n = int(input())
    edges = [[] for _ in range(n+1)]
    req = [0]*(n+1)
    for _ in range(n-1):
        u, v = map(int, input().split())
        edges[u].append(v)
        edges[v].append(u)
        req[u], req[v] = req[u]+1, req[v]+1
    stack = []
    for i in range(n+1):
        if req[i] == 1:
            stack.append(i)
    early = [False]*(n+1)
    while stack:
        u = stack.pop()
        if early[u]:
            for v in edges[u]:
                req[v] -= 1
                if req[v] == 1:
                    stack.append(v)
        else:
            for v in edges[u]:
                req[v] -= 1
                if req[v] == 1:
                    stack.append(v)
                early[v] = True
    print(sum(early))
main()
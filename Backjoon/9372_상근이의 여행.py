# 최소 신장 트리


# DFS를 사용한 풀이. 스택에 추가하기 전 방문체크를 해줘야한다.
# 그렇지 않으면 경로가 중복체크 되어버린다.

# 메모리: 32140KB / 시간: 152ms
from sys import stdin


input = stdin.readline

def dfs(route, n):
    stack = [1]
    visited = [False] * (n+1)
    visited[1] = True
    cnt = 0

    while stack:
        curr = stack.pop()
        for node in route[curr]:
            if not visited[node]:
                visited[node] = True  # 보통의 DFS는 pop한 뒤 방문체크를 하지만, 이 문제에서는 append하기 전에 해줘야한다.
                stack.append(node)
                cnt += 1
    return cnt

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    route = [[] for _ in range(N + 1)]

    for _ in range(M):
        a, b = map(int, input().split())
        route[a].append(b)
        route[b].append(a)

    print(dfs(route, N))


# 그런데... 문제를 잘 보면, N개의 노드를 연결하는 최소한의 간선수는 N-1이다.
# 즉 무조건 N-1을 반환하면 된다...

# 적절한 풀이는 아니지만 어쨌든 항상 답이 되는 풀이다 ㅎㅎㅎ
# 메모리: 31120KB / 시간: 128ms
from sys import stdin


input = stdin.readline
T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    for _ in range(M):
        a, b = map(int, input().split())
    print(N-1)
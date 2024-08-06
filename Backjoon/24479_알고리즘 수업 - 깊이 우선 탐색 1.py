# 그래프와 순회

# 메모리: 67996 / 시간: 592ms

import sys


sys.setrecursionlimit(10**6)  # 재귀 깊이 제한 증가
input = sys.stdin.readline
N, M, R = map(int, input().split())

graph = [[] for _ in range(N+1)]  # 인접 정점들을 기록할 빈 2차원 리스트 생성

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)  # 양방향 그래프이므로 u, v 모두에 더해준다.
    graph[v].append(u)

for i in range(1, N+1):
    graph[i].sort()  # 오름차순으로 정렬

visited = [0] * (N+1)
order = 1

def dfs(r: int):
    global order
    visited[r] = order  # visited[r]에 order 할당 후 order을 1 증가시킨다.
    order += 1

    for v in graph[r]:  # r의 인접 정점들에 대해, 만약 방문하지 않았다면 dfs(v) 실행.
        if not visited[v]:
            dfs(v)

dfs(R)

print(*visited[1:], sep="\n")


# 재귀 대신 스택을 사용한 풀이. 현재 Python 실행시간 1위인 코드.
import sys
input = sys.stdin.read
sys.setrecursionlimit(200000)

def dfs_stack(graph, start):
    visited = [0] * len(graph)
    stack = [start]
    order = 1
    while stack:
        node = stack.pop()
        if visited[node] == 0:
            visited[node] = order
            order += 1
            for neighbor in sorted(graph[node], reverse=True):
                if visited[neighbor] == 0:
                    stack.append(neighbor)
    return visited

def main():
    data = input().split()
    n = int(data[0])
    m = int(data[1])
    r = int(data[2])
    
    graph = [[] for _ in range(n + 1)]
    index = 3
    for _ in range(m):
        u = int(data[index])
        v = int(data[index + 1])
        graph[u].append(v)
        graph[v].append(u)
        index += 2
    
    visited_order = dfs_stack(graph, r)
    
    for i in range(1, n + 1):
        print(visited_order[i])

if __name__ == "__main__":
    main()
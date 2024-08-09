# 그래프와 순회

# 1번 컴퓨터를 통해 감염된 컴퓨터의 갯수를 출력.
# 메모리: 31120KB / 시간: 32ms

from sys import stdin


input = stdin.readline
N, M = int(input()), int(input())
network = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, input().split())
    network[u].append(v)
    network[v].append(u)

visited = [False] * (N+1)

def checking():
    stack = [1]
    
    while stack:
        c = stack.pop()
        if not visited[c]:
            visited[c] = True
            for v in network[c]:
                if not visited[v]:
                    stack.append(v)
    
    return sum(visited) - 1  # 1번 컴퓨터는 결과에서 제외해야함.

print(checking())
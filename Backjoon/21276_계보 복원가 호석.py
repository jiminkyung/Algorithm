# 문제집 - 0x1A강 - 위상 정렬


# 문제: https://www.acmicpc.net/problem/21276

# 직계 자손-부모 관계의 노드들만 주어지는게 아님.
# 따라서 DFS로 풀이 시 시간초과가 나온다. 이 문제는 진입차수 + BFS 로 풀어야 통과할 수 있음.

# 메모리: 37136KB / 시간: 496ms
from sys import stdin
from collections import deque


input = stdin.readline

N = int(input())
names = input().rstrip().split()
# 이름과 번호를 매칭시킴
name_to_num = {name: i for i, name in enumerate(names)}  # 1. 이름 -> 번호
num_to_name = {v: k for k, v in name_to_num.items()}  # 2. 번호 -> 이름

graph = [[] for _ in range(N)]
in_degree = [0] * N  # 진입차수가 0인 사람이 시조

M = int(input())
for _ in range(M):
    child, ancester = input().rstrip().split()
    child, ancester = name_to_num[child], name_to_num[ancester]

    graph[ancester].append(child)
    in_degree[child] += 1

# 직계자손들을 기록할 리스트
direct_child = [[] for _ in range(N)]

# 시조들을 큐에 넣고 BFS 실행
root = [i for i in range(N) if in_degree[i] == 0]
queue = deque(root)

# 진입차수로 직계 자손을 계산
def bfs():
    while queue:
        curr = queue.popleft()

        for node in graph[curr]:
            in_degree[node] -= 1
            if in_degree[node] == 0:  # 진입차수가 0이 된다면 현재 노드의 직계자손인셈
                direct_child[curr].append(node)
                queue.append(node)


bfs()
root = [num_to_name[r] for r in root]  # 시조들의 번호를 이름으로 변환

print(len(root))
print(*sorted(root))

for name in sorted(names):
    num = name_to_num[name]
    children = sorted(num_to_name[child] for child in direct_child[num])
    print(name, len(children), *children)
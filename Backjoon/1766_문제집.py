# 문제집 - 0x1A강 - 위상 정렬


# 문제: https://www.acmicpc.net/problem/1766

# DFS로 큰 번호 -> 작은 번호 순으로 풀어나가게끔 작성했지만 실패함.
# DFS 반례 👉 https://www.acmicpc.net/board/view/133051

# deque 모듈을 사용하지 않는 BFS 혹은 heapq + BFS 로 풀어야 시간초과 없이 통과 가능.

# 1. heapq + BFS
# 메모리: 41404KB / 시간: 176ms
from sys import stdin
from heapq import heappush, heappop


input = stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
in_degree = [0] * (N+1)


# 먼저 풀면 좋은 문제들 정리
for _ in range(M):
    A, B = map(int, input().split())

    graph[A].append(B)
    in_degree[B] += 1


heap = []

for i in range(1, N+1):
    if in_degree[i] == 0:  # 진입차수가 0인 문제들을 큐에 추가
        heappush(heap, i)


def bfs():
    ret = []

    while heap:
        # ✅ 현재 큐에서 가장 작은 번호를 뽑음.
        # => 큐에 존재하는 문제는 모두 당장 풀 수 있는 문제들임.
        curr = heappop(heap)
        ret.append(curr)

        for node in graph[curr]:
            in_degree[node] -= 1
            if in_degree[node] == 0:
                heappush(heap, node)
    
    return ret


print(*bfs())


# 2. 리스트를 사용하는 BFS
# deque를 사용할경우 매번 deque(sorted(queue))를 실행하므로 메모리 할당량이 늘어남.
# 메모리: 39328KB / 시간: 3376ms
from sys import stdin


input = stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
in_degree = [0] * (N+1)


# 먼저 풀면 좋은 문제들 정리
for _ in range(M):
    A, B = map(int, input().split())

    graph[A].append(B)
    in_degree[B] += 1


queue = []

for i in range(1, N+1):
    if in_degree[i] == 0:
        queue.append(i)


def bfs():
    ret = []

    while queue:
        # ✅ 정렬한 큐에서 제일 작은 번호를 뽑아냄.
        queue.sort()

        curr = queue.pop(0)
        ret.append(curr)

        for node in graph[curr]:
            in_degree[node] -= 1
            if in_degree[node] == 0:
                queue.append(node)
    
    return ret


print(*bfs())
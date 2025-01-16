# 문제집 - 0x0D강 - 시뮬레이션


# 문제: https://www.acmicpc.net/problem/17471

# 의외로 애먹었던 문제.
# 연결된 간선이 없는 구역도 지역구가 될 수 있음. (0으로 주어진 구역)
# 반례1👉 https://www.acmicpc.net/board/view/54133
# 반례2👉 https://www.acmicpc.net/board/view/149644

# 1. DFS 함수로 조합 생성
# 메모리: 32412KB / 시간: 40ms
from sys import stdin


input = stdin.readline

N = int(input())

# 인구 수, 간선 저장
people = [0] + list(map(int, input().split()))
graph = [[] for _ in range(N+1)]

for i in range(1, N+1):
    data = list(map(int, input().split()))
    for j in range(1, data[0] + 1):  # 양방향 그래프
        graph[i].append(data[j])
        graph[data[j]].append(i)


# 선거구 내 지역이 연결되어있는지 확인
def bfs(root: int, union: list) -> bool:
    visited = {root}
    curr = [root]

    while curr:
        nxt = []
        for node in curr:
            for nxt_node in graph[node]:
                if nxt_node in union and nxt_node not in visited:
                    visited.add(nxt_node)
                    nxt.append(nxt_node)
        curr = nxt
    
    return len(visited) == len(union)


# DFS로 조합 생성
min_diff = float("inf")
used = [False] * (N+1)

def dfs(A: list, start: int):
    global min_diff

    # A의 갯수가 1개 이상 N//2개 이하라면 인구 수 비교
    # (1, 2) / (3, 4, 5) 일때의 차이값과 (3, 4, 5) / (1, 2) 일때의 차이값은 같으므로 절반까지만 구해보면 된다.
    if 1 <= len(A) <= N//2:
        B = [i for i in range(1, N+1) if not used[i]]

        if not B:
            return
        
        # 두 구역 모두 인접해있는지 확인
        if bfs(A[0], A) and bfs(B[0], B):
            sum_A = sum(people[a] for a in A)
            sum_B = sum(people[b] for b in B)
            min_diff = min(abs(sum_A - sum_B), min_diff)
            if min_diff == 0:
                print(0)
                exit()
    
    for i in range(start, N+1):
        used[i] = True
        A.append(i)
        dfs(A, i+1)
        A.pop()
        used[i] = False


dfs([], 1)
print(min_diff if min_diff != float("inf") else -1)


# 2. combinations 모듈로 조합 생성
# 확실히 모듈을 사용하는게 가독성은 좋다.
# 메모리: 32412KB / 시간: 44ms
from sys import stdin
from itertools import combinations


input = stdin.readline

N = int(input())

# 인구 수, 간선 저장
people = [0] + list(map(int, input().split()))
graph = [[] for _ in range(N+1)]

for i in range(1, N+1):
    data = list(map(int, input().split()))
    for j in range(1, data[0] + 1):  # 양방향 그래프
        graph[i].append(data[j])
        graph[data[j]].append(i)


# 선거구 내 지역이 연결되어있는지 확인
def bfs(root: int, union: list) -> bool:
    visited = {root}
    curr = [root]

    while curr:
        nxt = []
        for node in curr:
            for nxt_node in graph[node]:
                if nxt_node in union and nxt_node not in visited:
                    visited.add(nxt_node)
                    nxt.append(nxt_node)
        curr = nxt
    
    return len(visited) == len(union)


# combinations 모듈로 조합 생성
min_diff = float("inf")

for size in range(1, N//2 + 1):  # A, B 각 조합의 순서가 바뀌어도 값은 동일하므로 절반까지만 생성함
    for comb in combinations(range(1, N+1), size):
        A = list(comb)
        B = list(i for i in range(1, N+1) if i not in comb)

        if bfs(A[0], A) and bfs(B[0], B):
            sum_A = sum(people[a] for a in A)
            sum_B = sum(people[b] for b in B)
            min_diff = min(abs(sum_A - sum_B), min_diff)
            if min_diff == 0:
                print(0)
                exit()


print(min_diff if min_diff != float("inf") else -1)
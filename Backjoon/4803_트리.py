# 트리


# 처음 코드. 단방향으로만 저장해줬으나 틀렸다.
# 반례 - 길이가 1인 사이클. 출처: https://www.acmicpc.net/board/view/19906
"""
3 3
1 1
2 2
3 3
결과: No Trees.
답: A forest of 3 trees.
"""
import sys
from collections import deque


input = sys.stdin.readline

def bfs(tree, visited, start):
    queue = deque([start])
    visited[start] = True
    node_cnt = edge_cnt = 0

    while queue:
        curr_node = queue.popleft()
        node_cnt += 1

        for node in tree[curr_node]:
            edge_cnt += 1
            if not visited[node]:
                visited[node] = True
                queue.append(node)
    
    return True if edge_cnt == node_cnt - 1 else False

order = 1
while True:
    n, m = map(int, input().split())

    if n == 0 and m == 0:
        break

    tree = [[] for _ in range(n+1)]
    # 루트노드로부터 왼쪽 서브트리, 오른쪽 서브트리
    # 부모-자식 두 노드의 경로는 유일하다.
    for _ in range(m):
        u, v = map(int, input().split())
        tree[u].append(v)
    
    visited = [False] * (n+1)
    ret = 0

    for i in range(1, n+1):
        if not visited[i]:
            if bfs(tree, visited, i):
                ret += 1
    
    print(f"Case {order}: ", end="")
    if ret == 0:
        print("No Trees.")
    elif ret == 1:
        print("There is one tree.")
    else:
        print(f"A forest of {ret} trees.")
    
    order += 1


# 위의 반례와 아래의 경우까지 해결하도록 수정하였으나 틀렸다.
"""
3 3
1 2
2 3
3 3
"""
import sys
from collections import deque


input = sys.stdin.readline

def bfs(tree, visited, start):
    queue = deque([start])
    visited[start] = True
    node_cnt = edge_cnt = 0

    while queue:
        curr_node = queue.popleft()
        node_cnt += 1

        for node in tree[curr_node]:
            if curr_node == node:  # 만약 3-3과 같이 자기루프(길이가 1인 사이클)이면 건너뛴다.
                continue
            edge_cnt += 1
            if not visited[node]:
                visited[node] = True
                queue.append(node)
    
    return True if edge_cnt == node_cnt - 1 else False

order = 1
while True:
    n, m = map(int, input().split())

    if n == 0 and m == 0:
        break

    tree = [[] for _ in range(n+1)]

    for _ in range(m):
        u, v = map(int, input().split())
        tree[u].append(v)
    
    visited = [False] * (n+1)
    ret = 0

    for i in range(1, n+1):
        if not visited[i]:
            if bfs(tree, visited, i):
                ret += 1
    
    print(f"Case {order}: ", end="")
    if ret == 0:
        print("No Trees.")
    elif ret == 1:
        print("There is one tree.")
    else:
        print(f"A forest of {ret} trees.")
    
    order += 1


# 무방향(양방향) 그래프로 작성하면 바로 통과한다.
# 왜 무방향 간선으로 저장해야하는가? 의문점이 있었으나 답을 찾았다.
"""
81 43
25 43
"""
# 위와 같은 데이터가 주어졌을때, 단방향으로 저장하게 되면 트리가 2개인것으로 간주한다.
# 하지만 실제로는 하나의 트리다.
# 81 -> 43 <- 25 는 사이클이 되는것아닌가? 싶었으나... 81 <- 43 -> 25 로 생각하면 트리 조건을 만족한다.
# 즉, 부모-자식 순서대로 데이터가 주어지는 것이 아니다. (이걸 왜 이제 깨달았을까?...)


# ⭐ 무방향 그래프로 수정한 결과

# 메모리: 37180KB / 시간: 200ms
import sys
from collections import deque


input = sys.stdin.readline

def bfs(tree, visited, start):
    queue = deque([start])
    visited[start] = True
    node_cnt = edge_cnt = 0
    
    while queue:
        curr_node = queue.popleft()
        node_cnt += 1
        
        for node in tree[curr_node]:
            edge_cnt += 1
            if not visited[node]:
                visited[node] = True
                queue.append(node)
    
    # 간선은 양방향으로 저장되므로 2로 나누어준다.
    edge_cnt //= 2
    
    # 트리 조건: 간선 수는 정점 수 - 1이어야 함
    return True if edge_cnt == node_cnt-1 else False

order = 1
while True:
    n, m = map(int, input().split())

    if n == 0 and m == 0:
        break

    tree = [[] for _ in range(n + 1)]

    for _ in range(m):
        u, v = map(int, input().split())
        tree[u].append(v)
        tree[v].append(u)  # 양방향 간선 저장
    
    visited = [False] * (n + 1)
    ret = 0

    for i in range(1, n + 1):
        if not visited[i]:
            if bfs(tree, visited, i):
                ret += 1

    print(f"Case {order}: ", end="")
    if ret == 0:
        print("No trees.")
    elif ret == 1:
        print("There is one tree.")
    else:
        print(f"A forest of {ret} trees.")
    
    order += 1


# 실행시간 1위 코드 참고👉 https://www.acmicpc.net/source/71373921
# 메모리: 37064KB / 시간: 156ms
import sys


def dfs(node, parent, tree, visited):
    # 스택을 사용하여 반복적인 DFS 탐색 수행
    stack = [(node, parent)]  # (현재 노드, 부모 노드) 튜플을 스택에 추가
    while stack:
        curr_node, parent_node = stack.pop()
        
        if visited[curr_node]:
            continue
        
        visited[curr_node] = True
        
        for neighbor in tree[curr_node]:
            if not visited[neighbor]:
                # 인접 노드가 아직 방문되지 않았다면 스택에 추가
                stack.append((neighbor, curr_node))
            elif neighbor != parent_node:
                # 인접 노드가 부모 노드가 아니라면 사이클이 존재
                return False
    
    # 사이클이 발견되지 않으면 True 반환
    return True

# 그래프에서 트리의 개수를 계산하는 함수
def solve(n, tree):
    visited = [False] * (n + 1)
    tree_count = 0
    
    # 모든 노드를 순회하며, 방문되지 않은 노드에서 DFS 수행
    for i in range(1, n + 1):
        if not visited[i]:
            # DFS를 호출하여 사이클이 없으면 트리로 간주
            if dfs(i, -1, tree, visited):  # 루트 노드의 부모를 -1로 설정
                tree_count += 1
    
    return tree_count

def print_answer(tc, answer):
    index_string = f"Case {tc}: "
    
    if answer == 0:
        print(index_string + "No trees.")
    elif answer == 1:
        print(index_string + "There is one tree.")
    else:
        print(index_string + f"A forest of {answer} trees.")

def main():
    input = sys.stdin.readline
    
    # 첫 번째 테스트 케이스 읽기
    n, m = map(int, input().split())
    tc = 1

    while not (n == 0 and m == 0):
        tree = [[] for _ in range(n + 1)]
        
        for _ in range(m):
            x, y = map(int, input().split())
            tree[x].append(y)
            tree[y].append(x)

        # 트리의 개수를 계산
        answer = solve(n, tree)
        
        print_answer(tc, answer)

        # 다음 테스트 케이스를 위해 변수 초기화
        tc += 1
        n, m = map(int, input().split())

main()
# 문제집 - 0x19강 - 트리


# 문제: https://www.acmicpc.net/problem/2250

# 처음에는 왼쪽 자식이 포함하는 노드의 갯수, 오른쪽 자식이 포함하는 노드의 갯수를 DFS를 통해 구한 뒤 열 번호를 매김.
# 알고보니 ⭐ 중위순회 순서 = 해당 노드의 열 위치

# 메모리: 34456KB / 시간: 60ms
from sys import stdin


input = stdin.readline

N = int(input())
INF = float("inf")

tree = [[] for _ in range(N+1)]
parent = [-1] * (N+1)  # parent[x]: x의 부모 노드

for _ in range(N):
    node, left, right = map(int, input().split())
    tree[node] = [left, right]

    if left != -1:
        parent[left] = node
    if right != -1:
        parent[right] = right

root = 0

level = [0] * (N+1)
level_max = [-INF] * (N+1)
level_min = [INF] * (N+1)

curr = 0

# 루트 노드 찾기
for i in range(1, N+1):
    if parent[i] == -1:
        root = i

# 루트 노드의 레벨을 1로 설정
level[root] = 1


def in_order(node):
    global curr

    left, right = tree[node]

    # 왼쪽 자식이 존재한다면 재귀
    if left != -1:
        level[left] = level[node] + 1
        in_order(left)
    
    curr += 1  # 노드 번호 증가

    lv = level[node]  # 현재 노드의 레벨
    level_min[lv] = min(level_min[lv], curr)
    level_max[lv] = max(level_max[lv], curr)

    if right != -1:
        level[right] = level[node] + 1
        in_order(right)


in_order(root)

ret_level = ret_width = 0

for i in range(1, N+1):
    # 끝 레벨까지 탐색했다면 break
    if level_max[i] == -INF or level_min[i] == INF:
        break

    diff = level_max[i] - level_min[i] + 1
    if ret_width < diff:
        ret_width = diff
        ret_level = i


print(ret_level, ret_width)
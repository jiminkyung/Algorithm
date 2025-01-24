# 문제집 - 0x19강 - 트리


# 문제: https://www.acmicpc.net/problem/22856

# 스택만 사용해서 풀다가 실패...
# 다른 풀이를 참고해서 작성

# 메모리: 53412KB / 시간: 252ms
from sys import stdin


input = stdin.readline

N = int(input())

tree = {}  # tree[a] = [b, c]
parent = [-1] * (N+1)  # parent[a]: a의 부모 노드

for _ in range(N):
    a, b, c = map(int, input().split())
    tree[a] = [b, c]
    
    if b != -1:
        parent[b] = a
    if c != -1:
        parent[c] = a

# 마지막 노드 구하기
end = 1
while tree[end][1] != -1:
    end = tree[end][1]


def counting():
    visited = [False] * (N+1)
    curr = 1
    cnt = 0
    
    while True:
        visited[curr] = True  # 현재 노드 방문처리
        
        left, right = tree[curr]

        # 만약 현재 노드가 마지막 노드고, 왼쪽/오른쪽 자식이 없거나 방문한상태라면 break
        if curr == end and (
            left == -1 or visited[left]) and (
            right == -1 or visited[right]):
            break
            
        if left != -1 and not visited[left]:
            curr = left
            cnt += 1
        elif right != -1 and not visited[right]:
            curr = right
            cnt += 1
        elif parent[curr] != -1:
            curr = parent[curr]
            cnt += 1
            
    return cnt


print(counting())


# 훨씬 간단한 코드!
# 노드 방문 횟수를 미리 계산해놓은 방식.
# 각 노드는 기본적으로 2번씩 방문, 루트부터 오른쪽 리프노드까지의 경로 노드들은 1번씩만 방문한것으로 계산.
# 출처: https://www.acmicpc.net/source/68906988
def cnt_visited():
    from sys import stdin
    N = int(stdin.readline())
    if N == 1:
        return 0

    right_child = [0] * (N + 1)
    for _ in range(N):
        a, b, c = map(int, stdin.readline().split())
        right_child[a] = c

    cnt_list = [2] * (N + 1)
    right_root = 1

    while True:
        if right_child[right_root] != -1:
            right_root = right_child[right_root]
            cnt_list[right_root] = 1
        else:
            return sum(cnt_list[2:])

print(cnt_visited())
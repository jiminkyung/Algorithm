# 문제집 - 0x19강 - 트리


# 문제: https://www.acmicpc.net/problem/1068
# 메모리: 32412KB / 시간: 40ms
from sys import stdin


input = stdin.readline

N = int(input())

parent = list(map(int, input().split()))  # parent[x]: x의 부모 노드
child = [[] for _ in range(N)]  # child[x] = [x의 자식 노드]

D = int(input())

# 자식 노드들 추가
for c, p in enumerate(parent):
    # p: 부모노드, c: 자식노드
    # D가 자식노드 리스트에 들어가지 않게끔 처리
    if p != -1 and c != D:
        child[p].append(c)

# 자식노드 리스트 삭제
def delete(node):
    parent[node] = -2  # 삭제할 노드의 parent값을 -2로 설정

    if not child[node]:
        return
    
    for c in child[node]:
        delete(c)
    child[node] = []  # 현재 노드의 재귀가 끝나면 리스트를 비워줌(삭제)

delete(D)
cnt = 0

for i in range(N):
    # 자식 리스트가 비어있고, parent값이 -2가 아니라면 리프노드
    if not child[i] and parent[i] != -2:
        cnt += 1

print(cnt)
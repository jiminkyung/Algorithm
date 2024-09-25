# 기하 2


# 문제: https://www.acmicpc.net/problem/2162

# 처음 코드. 예시 데이터부터 틀림 => 연속된 두 선분만 비교하는것이 아니라, 모든 선분을 비교해야한다.
from sys import stdin


input = stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    fa, fb = find(a), find(b)

    if fa != fb:
        if rank[fa] < rank[fb]:
            parent[fa] = fb
        elif rank[fa] > rank[fb]:
            parent[fb] = fa
        else:
            parent[fb] = fa
            rank[fa] += 1

def ccw(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])

def check(p1, p2, q1, q2, ret1, ret2):
    if ret1 == 0 and ret2 == 0:
        return p2 >= q1 and p1 <= q2
    return ret1 <= 0 and ret2 <= 0

N = int(input())
point = []

for _ in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    if (x1, y1) > (x2, y2):
        x1, y1, x2, y2 = x2, y2, x1, y1
    point.append((x1, y1))
    point.append((x2, y2))

parent = list(range(N))
rank = [1] * N

for i in range(0, N, 2):
    ret1 = ccw(point[i], point[i+1], point[i+2]) * ccw(point[i], point[i+1], point[i+3])
    ret2 = ccw(point[i+2], point[i+3], point[i]) * ccw(point[i+2], point[i+3], point[i+1])

    if check(point[i], point[i+1], point[i+2], point[i+3], ret1, ret2):
        union(i//2, i//2 + 1)

print(len(set(parent)), max(rank), sep="\n")


# 수정한 두번째 코드. 통과!
# 참고한 반례👉 https://www.acmicpc.net/board/view/91251
# ⭐ 마지막에 경로 압축을 한번 더 해줘야 한다.

# 메모리: 32140KB / 시간: 4468ms
from sys import stdin


input = stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    fa, fb = find(a), find(b)

    if fa != fb:
        if rank[fa] < rank[fb]:
            parent[fa] = fb
            rank[fb] += rank[fa]
        else:
            parent[fb] = fa
            rank[fa] += rank[fb]

def ccw(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])

def check(line1, line2):
    p1, p2 = line1
    q1, q2 = line2

    ret1 = ccw(p1, p2, q1) * ccw(p1, p2, q2)
    ret2 = ccw(q1, q2, p1) * ccw(q1, q2, p2)

    if ret1 == 0 and ret2 == 0:
        return p2 >= q1 and p1 <= q2
    return ret1 <= 0 and ret2 <= 0

N = int(input())
point = []

for _ in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    if (x1, y1) > (x2, y2):
        x1, y1, x2, y2 = x2, y2, x1, y1
    point.append(((x1, y1), (x2, y2)))

parent = list(range(N))
rank = [1] * N

for i in range(N):
    for j in range(i+1, N):
        if check(point[i], point[j]):
            union(i, j)

# 경로 압축을 한번 더 해줘야 한다. 모든 parent가 바로 루트 노드를 가르킬 수 있도록.
# 마지막 경로 압축 전 parent: [1, 1, 1, 1, 1, 1, 1, 0] / 후: [1, 1, 1, 1, 1, 1, 1, 1]
# 관련 설명 참고👉 https://www.acmicpc.net/board/view/112112
for i in range(N):
    parent[i] = find(parent[i])

print(len(set(parent)), max(rank), sep="\n")
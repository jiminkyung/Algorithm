# 문제집 - 0x18강 - 그래프


# 문제: https://www.acmicpc.net/problem/1043

# 유니온 파인드로 풀이.
# 메모리: 32412KB / 시간: 36ms
from sys import stdin


input = stdin.readline

N, M = map(int, input().split())

# 진실을 아는 사람
known = list(map(int, input().split()))
known_cnt = known[0]
known_people = known[1:] if known_cnt > 0 else []

# 유니온 파인드 사용
parent = list(range(N + 1))

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    a = find(x)
    b = find(y)
    if a != b:
        # 조건없이 parent[a] = b or parent[b] = a 로 묶어줘도 됨
        if a < b:
            parent[b] = a
        else:
            parent[a] = b


# 진실을 아는 사람들은 같은 집합으로 묶기 => 0번 노드를 기준으로 선정
for person in known_people:
    union(person, 0)

# 각 파티의 참석자 정보
parties = []
for _ in range(M):
    _, *people = map(int, input().split())
    parties.append(people)
    # 파티 참석자들을 같은 집합으로 묶기
    for i in range(1, len(people)):
        union(people[0], people[i])

# 과장된 이야기를 할 수 있는 파티 개수 계산
count = 0
for party in parties:
    # 이 파티에 참석한 사람 중 하나라도 진실 집합에 속하면 진실을 이야기해야 함
    # 단순히 parent[person] != 0 으로 비교하면 X
    # 진실을 2차로 알게 된 사람과 같은 파티에 참석했던 사람들을 반영하지못함
    if all(find(person) != find(0) for person in party):
        count += 1

print(count)
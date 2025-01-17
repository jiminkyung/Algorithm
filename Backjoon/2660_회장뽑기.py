# 문제집 - 0x18강 - 그래프


# 문제: https://www.acmicpc.net/problem/2660
# 메모리: 32412KB / 시간: 48ms
from sys import stdin


input = stdin.readline

N = int(input())
INF = float("inf")

member = [0] * (N+1)  # 회원들의 점수를 저장할 리스트
graph = [[INF] * (N+1) for _ in range(N+1)]

while True:
    m1, m2 = map(int, input().split())

    if (m1, m2) == (-1, -1):
        break

    # 친구사이이므로 양방향 저장
    graph[m1][m2] = 1
    graph[m2][m1] = 1

# 자기자신은 0으로 설정
for i in range(1, N+1):
    graph[i][i] = 0

# 플로이드-워셜 수행
for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            graph[i][j] = min(graph[i][k] + graph[k][j], graph[i][j])

# 점수 구하기
for m1 in range(1, N+1):
    max_dis = 0  # 가장 먼 친구까지의 거리 == 점수
    for m2 in range(1, N+1):
        max_dis = max(graph[m1][m2], max_dis)
    member[m1] = max_dis

score = min(member[1:])
cnt = member.count(score)  # 회원의 수는 50 이하이므로 count로 충분함
candidates = [i for i in range(1, N+1) if member[i] == score]

print(score, cnt)
print(*candidates)
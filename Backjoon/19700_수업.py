# 문제집 - 0x16강 - 이진 검색 트리


# 문제: https://www.acmicpc.net/problem/19700

# 통과 X
# 33%에서 TLE
from sys import stdin
from heapq import heappush, heappop


input = stdin.readline

N = int(input())
students = [tuple(map(int, input().split())) for _ in range(N)]
students.sort(reverse=True)

teams = []  # 최대 힙

for h, k in students:
    popped = []  # 빼놨던 팀들
    
    while teams:
        team = heappop(teams)
        if -team < k:
            heappush(teams, team - 1)
            break
        popped.append(team)
    else:
        heappush(teams, -1)
    
    # 빼놨던 팀들 다시 넣기
    for p in popped:
        heappush(teams, p)

print(len(teams))
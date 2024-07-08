# 백트래킹
# AI선생님과 함께한 풀이. itertools 모듈 사용 X

# 메모리: 31120KB / 시간: 2760ms

import sys


input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

ret = float("inf")

def calculator(team):
    return sum(arr[i][j] for i in team for j in team if i != j)

def backtrack(idx, start_team):
    global ret

    if len(start_team) == N//2:
        link_team = list(set(range(N)) - set(start_team))
        start_stat = calculator(start_team)
        link_stat = calculator(link_team)

        ret = min(ret, abs(start_stat - link_stat))
        return
    
    for i in range(idx, N):
        backtrack(i + 1, start_team + [i])

backtrack(0, [])
sys.stdout.write(str(ret))
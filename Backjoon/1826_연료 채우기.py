# 문제집 - BOJ 길라잡이 베타 (1)


# 문제: https://www.acmicpc.net/problem/1826
# 고민하다가 결국 다른 사람들의 풀이를 참고했다...

# 1. for문으로 한바퀴 돈 다음 남은 거리는 while문으로 체크하기
# 참고👉 https://www.acmicpc.net/source/82612894
# 메모리: 34212KB / 시간: 56ms
from sys import stdin
from heapq import heappop, heappush


input = stdin.readline

def solution():
    N = int(input())
    oils = sorted(list(map(int, input().split())) for _ in range(N))
    L, P = map(int, input().split())

    passed = []
    cnt = 0

    for d, o in oils:
        while P < d:
            if not passed:
                return -1
            P -= heappop(passed)[0]
            cnt += 1
        heappush(passed, (-o, d))

    while P < L:
        if not passed:
            return -1
        P -= heappop(passed)[0]
        cnt += 1
    return cnt

print(solution())


# 2. while문으로 L에 도달할때까지 반복하기
# 참고👉 https://dev-scratch.tistory.com/73
# 메모리: 34212KB / 시간: 68ms
from sys import stdin
from heapq import heappop, heappush


input = stdin.readline

N = int(input())
oils = sorted(list(map(int, input().split())) for _ in range(N))
L, P = map(int, input().split())

passed = []
idx = curr_loc = 0
cnt = 0

while (curr_loc + P < L):
    while idx < N and P >= oils[idx][0] - curr_loc:
        heappush(passed, (-oils[idx][1], oils[idx][0]))
        idx += 1
        continue

    if not passed:
        cnt = -1
        break
    else:
        o, d = heappop(passed)
        P -= d + o - curr_loc
        curr_loc = d
        cnt += 1

print(cnt)
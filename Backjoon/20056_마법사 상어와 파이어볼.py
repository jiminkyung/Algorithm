# 문제집 - 0x0D강 - 시뮬레이션


# 문제: https://www.acmicpc.net/problem/20056
# 메모리: 35540KB / 시간: 276ms
from sys import stdin
from collections import defaultdict


input = stdin.readline

# 순서대로 0 ~ 7 방향
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

N, M, K = map(int, input().split())

board = [[0] * N for _ in range(N)]
fireball = defaultdict(list)

for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    fireball[(r-1, c-1)].append((m, s, d))

# 1. 파이어볼 이동
def moving():
    # m: 질량, s: 속력, d: 방향
    new_fireball = defaultdict(list)
    for (r, c), v in fireball.items():
        for m, s, d in v:
            nr = (r + dx[d] * s) % N  # 범위를 벗어날 경우 이어지도록 처리
            nc = (c + dy[d] * s) % N
            new_fireball[(nr, nc)].append((m, s, d))
    return new_fireball


# 2. 파이어볼 분리
def separating():
    new_fireball = defaultdict(list)

    for k, v in fireball.items():
        if len(v) > 1:  # 파이어볼이 2개 이상이라면
            odd_even = [0, 0]  # 짝/홀을 구분할 리스트. 각각의 d를 2로 나눈 나머지값이 인덱스에 해당됨. [짝수인경우, 홀수인경우]
            new_m = new_s = 0
            for m, s, d in v:
                new_m += m
                new_s += s
                odd_even[d % 2] += 1
            new_m //= 5
            new_s //= len(v)

            if new_m == 0:  # 질량이 0이라면 소멸
                continue

            if 0 in odd_even:
                for i in range(0, 7, 2):
                    new_fireball[k].append((new_m, new_s, i))
            else:
                for i in range(1, 8, 2):
                    new_fireball[k].append((new_m, new_s, i))
        else:  # 파이어볼이 1개라면 변화 없이 그대로 다음턴까지
            new_fireball[k] = v
    return new_fireball

for _ in range(K):
    # 이 부분이 참 보기 싫은데, 메모리/실행시간 효율이 가장 좋은 버전이라 일단 킵...
    # 다시 수정해야할듯.
    fireball = moving()
    fireball = separating()

ret = sum(m for v in fireball.values() for m, _, _ in v)
print(ret)
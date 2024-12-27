# 문제집 - 0x13강 - 이분탐색


# 문제: https://www.acmicpc.net/problem/18869
# 메모리: 52348KB / 시간: 592ms
from sys import stdin


input = stdin.readline

M, N = map(int, input().split())
spaces = {}

for _ in range(M):
    space = tuple(map(int, input().split()))
    # 크기가 같은 행성들 => 동일한 순위로 처리해야함.
    # 반례👉 https://www.acmicpc.net/board/view/154125
    rank = {s: i for i, s in enumerate(sorted(set(space)))}
    sorted_space = tuple(rank[s] for s in space)
    # 행성들의 순위를 키값으로 설정, 동일한경우 카운트 +1
    spaces[sorted_space] = spaces.get(sorted_space, 0) + 1

same = 0
for r, cnt in spaces.items():
    if cnt > 1:
        same += cnt * (cnt-1) // 2

print(same)
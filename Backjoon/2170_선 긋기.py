# 문제집 - 0x11강 - 그리디


# 문제: https://www.acmicpc.net/problem/2170
# 처음엔 이전 (x, y) 범위 내에 현재 x값이 들어간다면, 현재 y값으로 기준값을 변경했으나 틀림.
# => 기준값 범위 내에 현재 (x, y)가 완전히 포함되는 형태라면 기준값 변경 없이 넘어가야함.
# => 반례 링크👉 https://www.acmicpc.net/board/view/123249

# 메모리: 173500KB / 시간: 2960ms
from sys import stdin


input = stdin.readline

N = int(input())
lines = [tuple(map(int, input().split())) for _ in range(N)]
lines.sort()

curr = [lines[0][0], lines[0][1]]
ret = 0

for i in range(1, N):
    s, e = lines[i]
    if s > curr[1]:
        ret += curr[1] - curr[0]
        curr = [s, e]
    else:
        curr[1] = max(curr[1], e)  # 현재 curr[1]과 e 중 더 큰값으로 업데이트

ret += curr[1] - curr[0]

print(ret)
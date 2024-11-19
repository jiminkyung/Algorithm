# 문제집 - 0x0D강 - 시뮬레이션


# 문제: https://www.acmicpc.net/problem/14891

# 메모리: 31120KB / 시간: 36ms
from sys import stdin


input = stdin.readline

gears = [list(map(int, input().rstrip())) for _ in range(4)]
K = int(input())
rotation = [list(map(int, input().split())) for _ in range(K)]

# 각 톱니바퀴가 맞닿는 부위는 [2], [-2]번 톱니.
def rotate(direction, gear, rotated):
    left, right = gears[gear][-2], gears[gear][2]

    if direction == 1:
        gears[gear] = gears[gear][-1:] + gears[gear][:-1]
    else:
        gears[gear] = gears[gear][1:] + gears[gear][:1]
    
    rotated.add(gear)

    if gear-1 >= 0 and gear-1 not in rotated and gears[gear-1][2] != left:
        rotate(-direction, gear-1, rotated)
    if gear+1 <= 3 and gear+1 not in rotated and gears[gear+1][-2] != right:
        rotate(-direction, gear+1, rotated)

for idx, direction in rotation:
    rotate(direction, idx-1, set())

# N극은 0, S극은 1
ret = [0 if gears[i][0] == 0 else 2**i for i in range(4)]
print(sum(ret))
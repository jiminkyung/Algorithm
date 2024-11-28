# 문제집 - 0x0D강 - 시뮬레이션


# 문제: https://www.acmicpc.net/problem/20057
# 메모리: 41308KB / 시간: 880ms
from sys import stdin


input = stdin.readline

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
# 방향값. 서, 남, 동, 북
directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
# y칸 주변으로 흩어지는 모래의 (x, y, 비율)
patterns = {0: [(-2, 0, 0.02), (2, 0, 0.02), (-1, 0, 0.07), (1, 0, 0.07),
               (-1, -1, 0.1), (1, -1, 0.1), (-1, 1, 0.01), (1, 1, 0.01), (0, -2, 0.05)]}


def rotate(pattern):
    """(x, y) => (-y, x) 반시계방향으로 90º 회전"""
    rotated = [(-y, x, per) for x, y, per in pattern]
    return rotated

# directions 순서와 똑같이
patterns[1] = rotate(patterns[0])
patterns[2] = rotate(patterns[1])
patterns[3] = rotate(patterns[2])

x = y = N//2
length = 1
# outside: 격자 밖으로 뿌려진 모래, dir: 현재 방향값
outside = dir = 0
is_finished = False

def spread(x, y, dir):
    global outside
    
    # 현재 칸의 모래
    sand = graph[x][y]
    # 현재 칸으로부터 뿌려진 모래의 양
    spreaded = 0

    for dx, dy, per in patterns[dir]:
        new_sand = int(sand * per)
        nx, ny = x + dx, y + dy

        # 범위 내라면 해당 좌표에 더해주고, 벗어난다면 outside에 더해준다.
        # 뿌려진 모래의 양은 범위와 상관없이 기록
        if 0 <= nx < N and 0 <= ny < N:
            graph[nx][ny] += new_sand
        else:
            outside += new_sand
        spreaded += new_sand
    
    # 현재 모래의 양에서 뿌려진 모래의 양을 뺀 다음 이 값을 조건에 맞게 더해줌.
    ax, ay = x + directions[dir][0], y + directions[dir][1]
    if 0 <= ax < N and 0 <= ay < N:
        graph[ax][ay] += sand - spreaded
    else:
        outside += sand - spreaded
    
    graph[x][y] -= spreaded


while not is_finished:
    # 두번씩(좌/하, 우/상) length만큼 반복
    for _ in range(2):
        for _ in range(length):
            # x → y 토네이도 이동
            nx, ny = x + directions[dir][0], y + directions[dir][1]
            spread(nx, ny, dir)
            x, y = nx, ny
            # (0, 0)에 도착하면 플래그를 True로 변경 후 break
            if x == 0 and y == 0:
                is_finished = True
                break
        if is_finished:
            break
        # length만큼 이동 후 방향을 90º 틀어줌
        dir = (dir + 1) % 4
    # 두번의 반복이 끝나면 length에 1 더해줌
    length += 1

print(outside)
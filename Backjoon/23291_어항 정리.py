# 문제집 - 0x0D강 - 시뮬레이션


# 문제: https://www.acmicpc.net/problem/23291

# 1. 물고기 수가 최소인 어항들에 한마리씩 투하
# 2-1. 가장 왼쪽에 있는 어항 들어서 오른쪽 위에 올려둠
# 2-2. 2개 이상 쌓여있는 어항을 들어서 시계방향으로 90도 회전
# 2-3. 바닥어항위에 올려둠. 왼쪽부터. 공중부양한 어항의 가장 오른쪽 밑에 바닥 어항이 있을때까지.
# 3. 물고기 수 조절. 모든 인접한 두 어항의 차이 / 5 = d일때, d가 0보다 크면 둘 중 더 적게 있는 쪽에 d마리를 넘겨줌.
# 4. 어항을 다시 일렬로 놓음. 왼쪽 -> 오른쪽, 아래 -> 위. 열을 중심으로 행을 아래에서 위로 진행시키면 될듯?
# 5. 왼쪽 절반을 시계방향으로 180도 회전 후 오른쪽 절반 위에 놓음. 두번 반복!
# 6. 물고기 수 조절.
# 7. 어항을 다시 일렬로...
# ====> 물고기가 가장 많은 어항의 고기수 - 가장 적은 어항의 고기수 <= K 가 되려면 몇번해야되는지...

# 메모리: 32412KB / 시간: 40ms
from sys import stdin


input = stdin.readline


N, K = map(int, input().split())
tank = list(map(int, input().split()))

count = 0

# 🚨 함수를 while문 안에 넣으면 매번 생성되므로 오버헤드 가능성이 있음.
def rotate(arr: list) -> list:
    """ 시계방향으로 90º 회전 """
    n, m = len(arr), len(arr[0])
    return [[arr[n-1-j][i] for j in range(n)] for i in range(m)]

def divide(tank: list) -> list:
    """ 물고기 수 조절 후 새로운 어항 반환 """
    new_tank = [line[:] for line in tank]

    dx = [0, 1]
    dy = [1, 0]

    for x in range(len(tank)):
        for y in range(len(tank[x])):
            # 이미 체크한 어항끼리는 다시 체크 X
            # 오른쪽, 아래 두 방향으로만 진행해도 충분할듯.
            for i in range(2):
                nx = x + dx[i]
                ny = y + dy[i]

                # 새로운 좌표의 행이 어항의 행을 벗어나지 않고, 열이 해당 행의 열을 벗어나지 않을 경우에만 진행
                if not (0 <= nx < len(tank) and 0 <= ny < len(tank[nx])):
                    continue

                d = abs(tank[x][y] - tank[nx][ny]) // 5
                if d > 0:
                    if tank[x][y] > tank[nx][ny]:
                        new_tank[x][y] -= d
                        new_tank[nx][ny] += d
                    else:
                        new_tank[x][y] += d
                        new_tank[nx][ny] -= d
    return new_tank


def turn(tank: list) -> list:
    """ 어항을 일렬로 되돌림 """
    new_tank = []
    for col in range(len(tank[-1])):  # 열을 0부터
        for row in range(len(tank)-1, -1, -1):  # 행은 아래 -> 위로
            if col < len(tank[row]):  # 해당 행의 열 범위 내에 있다면
                new_tank.append(tank[row][col])
    return new_tank


while True:
    # 물고기 수 차이가 K 이하가 되면 멈춰~
    if max(tank) - min(tank) <= K:
        break
    # 1. 물고기 추가
    min_fish = min(tank)
    for i in range(N):
        if tank[i] == min_fish:
            tank[i] += 1

    # 2. 돌리기
    tank = [[tank[0]], tank[1:]]
    while True:
        l = len(tank[0])
        air_tank = [tank[i][:l] for i in range(len(tank))]  # 공중부양 어항
        floor = tank[-1][l:]  # 바닥 어항

        air_tank = rotate(air_tank)

        if len(air_tank[0]) > len(floor):  # 공중부양 어항의 길이가 바닥 어항보다 길면 break
            break

        tank = [*air_tank, floor]


    # 3. 물고기 수 조절
    tank = divide(tank)

    # 4. 어항 일렬로 놓기
    tank = turn(tank)

    # 5. 다시 공중부양
    l = len(tank) // 2

    tmp = tank[:l][::-1]  # 첫번째 돌리기. 일렬이니까 반대로 뒤집어주면 됨.
    new_tank = [tmp, tank[l:]]

    l //= 2

    tmp = rotate([new_tank[0][:l], new_tank[1][:l]])  # 두번째 돌리기는 90º회전을 두번
    tmp = rotate(tmp)
    tank = tmp + [new_tank[0][l:], new_tank[1][l:]]

    # 6. 다시 물고기 조절 후 일렬로
    tank = divide(tank)
    tank = turn(tank)

    count += 1


print(count)
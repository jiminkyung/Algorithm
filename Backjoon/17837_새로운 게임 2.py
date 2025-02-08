# 문제집 - 0x0D강 - 시뮬레이션


# 문제: https://www.acmicpc.net/problem/17837

# 처음에 틀렸던 이유
# 1. 처음에 orders 값을 저장할 때, position을 업데이트 한 다음 그대로 `len(position[좌표])` 사용.
# => 이렇게되면 0번째 말이더라도 이미 position에 추가한 다음이기에 order은 1이 됨 ㅜ
# 2. 빨간색 칸일 경우 horse 자체를 뒤집어줘야함.
# => 뒤집힌 순서대로 order 업데이트를 진행해야함. 하지만 나는 position에만 뒤집어서 추가하고 order 업데이트는 기존 순서 그대로 사용...

# 메모리: 35068KB / 시간: 68ms
from sys import stdin
from collections import defaultdict


input = stdin.readline

N, K = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(N)]

# 말들의 위치와 방향, 순서
horses = [0] * (K + 1)
orders = [0] * (K + 1)
position = defaultdict(list)

# 방향 벡터 (→, ←, ↑, ↓)
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
reverse = [1, 0, 3, 2]  # 방향을 뒤집을경우

# 말들의 위치와 방향, 해당 칸에서 몇번째에 위치하는지 저장
for i in range(1, K + 1):
    r, c, d = map(int, input().split())
    horses[i] = (r-1, c-1, d-1)
    position[(r-1, c-1)].append(i)
    orders[i] = len(position[(r-1, c-1)]) - 1

# 격자 범위 체크
def checking(nx, ny):
    return 0 <= nx < N and 0 <= ny < N

# 말 이동
def moving():
    for i in range(1, K + 1):
        x, y, d = horses[i]
        order = orders[i]
        horse_stack = position[(x, y)][order:]  # 현재 말과 위에 있는 말들 가져오기
        position[(x, y)] = position[(x, y)][:order]  # 이동할 말을 현재 칸에서 제외시킴

        nx, ny = x + dx[d], y + dy[d]

        # 범위 밖 or 이동할 칸이 파란색이면 방향 변경
        if not checking(nx, ny) or field[nx][ny] == 2:
            d = reverse[d]
            horses[i] = (x, y, d)  # 방향만 갱신시켜둠
            nx, ny = x + dx[d], y + dy[d]

            # 여전히 파란색이면 이동 X, 복귀시킴
            if not checking(nx, ny) or field[nx][ny] == 2:
                position[(x, y)].extend(horse_stack)
                continue
        
        # 새로운 칸에서는 몇번째인지 계산
        new_order = len(position[(nx, ny)])

        # 흰색 -> 그대로
        if field[nx][ny] == 0:
            position[(nx, ny)].extend(horse_stack)
        # 빨간색 -> 뒤집어줌
        elif field[nx][ny] == 1:
            horse_stack = horse_stack[::-1]
            position[(nx, ny)].extend(horse_stack)

        # 이동한 말들의 정보 갱신
        # 방향은 기존 그대로, 좌표와 순서만 변경
        for idx, h in enumerate(horse_stack):
            horses[h] = (nx, ny, horses[h][2])
            orders[h] = new_order + idx

        # 말이 4개 이상 쌓였다면 게임 끝
        if len(position[(nx, ny)]) >= 4:
            return False
    return True


turn = 0

while turn < 1000:
    turn += 1

    if not moving():
        print(turn)
        break
else:
    print(-1)


# GPT에게 더 좋은 방법을 찾아보라고 시킨 결과물.
# index()함수를 사용하니까 order을 따로 관리해주지 않아도 됨.
# horse는 딕셔너리로, position은 리스트로 관리함. 근데 틀은 내 원래 코드와 같은듯...?
from sys import stdin
from collections import defaultdict

input = stdin.readline

N, K = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(N)]

# 말들의 위치와 방향 저장
horses = {}  # {말 번호: (x, y, 방향)}
position = [[[] for _ in range(N)] for _ in range(N)]  # 체스판에 쌓인 말 저장

# 이동 방향: →, ←, ↑, ↓
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
reverse = [1, 0, 3, 2]  # 방향 반전

for i in range(1, K+1):
    r, c, d = map(int, input().split())
    horses[i] = (r-1, c-1, d-1)
    position[r-1][c-1].append(i)  # 해당 칸에 말 추가

def checking(nx, ny):
    return 0 <= nx < N and 0 <= ny < N

def moving():
    for i in range(1, K+1):
        x, y, d = horses[i]

        # 현재 위치에서 말 리스트 가져오기
        idx = position[x][y].index(i)  # i번 말이 실제로 몇 번째인지 찾기
        horse_stack = position[x][y][idx:]  # i번 말과 그 위의 말들 이동
        position[x][y] = position[x][y][:idx]  # 남은 말만 유지

        # 이동할 좌표
        nx, ny = x + dx[d], y + dy[d]

        # 파란색이거나 범위 벗어나면 방향 바꿔서 재이동
        if not checking(nx, ny) or field[nx][ny] == 2:
            d = reverse[d]  # 현재 말의 방향만 바꾸기
            horses[i] = (x, y, d)  # 방향 업데이트
            nx, ny = x + dx[d], y + dy[d]

            if not checking(nx, ny) or field[nx][ny] == 2:  # 반대 방향도 막히면 이동 안 함
                position[x][y].extend(horse_stack)  # 원래 자리로 되돌리기
                continue

        # 흰색: 그대로 쌓기
        if field[nx][ny] == 0:
            position[nx][ny].extend(horse_stack)
        # 빨간색: 순서 뒤집어서 쌓기
        elif field[nx][ny] == 1:
            position[nx][ny].extend(horse_stack[::-1])

        # 이동한 모든 말의 위치 갱신
        for h in horse_stack:
            horses[h] = (nx, ny, horses[h][2])  # 위치만 변경

        # 말 4개 이상 쌓이면 종료
        if len(position[nx][ny]) >= 4:
            return False

    return True

turn = 0

while turn < 1000:
    turn += 1

    if not moving():
        print(turn)
        break
else:
    print(-1)
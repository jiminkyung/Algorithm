# 문제집 - 0x0D강 - 시뮬레이션


# 문제: https://www.acmicpc.net/problem/15898

# Python3, PyPy3 모두 통과하지 못함. 시간초과 문제.
# 시도한 방법
# => 회전 배열들을 미리 만들어두기
# => 가지치기(제대로 처리되지 못함... 경우의 수가 많아 의미가 없다.)

# PyPy3로 통과한분이 딱 한분 계시긴 함. 많은 최적화가 필요하다고 한다...

# 1) 색상들을 정수값으로 변환, 품질 배열과 색상 배열로 분리
from sys import stdin


input = stdin.readline

N = int(input())

C = {"W": 0, "R": 1, "G": 2, "B": 3, "Y": 4}
val_arr = [[0] * 5 for _ in range(5)]
col_arr = [[0] * 5 for _ in range(5)]
values = []
colors = []

for _ in range(N):
    value = [list(map(int, input().split())) for _ in range(4)]
    color = [[C[c] for c in input().rstrip().split()] for _ in range(4)]

    values.append(value)
    colors.append(color)


# 90º 회전 함수
def rotate(field: list) -> list:
    return [[field[3-j][i] for j in range(4)] for i in range(4)]


# 선택한 재료를 가마에 투입시키는 함수
def put(val_arr: list, col_arr: list, val: list, col: list, x: int, y: int) -> list:
    new_val_arr = [line[:] for line in val_arr]
    new_col_arr = [line[:] for line in col_arr]

    for i in range(4):
        for j in range(4):
            new_val_arr[x+i][y+j] += val[i][j]

            if new_val_arr[x+i][y+j] < 0:
                new_val_arr[x+i][y+j] = 0
            elif new_val_arr[x+i][y+j] > 9:
                new_val_arr[x+i][y+j] = 9

            if col[i][j] != 0:
                new_col_arr[x+i][y+j] = col[i][j]
    return new_val_arr, new_col_arr


# 가마 점수 계산 함수
def counting(val_arr, col_arr):
    score = [0] * 5

    for i in range(5):
        for j in range(5):
            score[col_arr[i][j]] += val_arr[i][j]
    R, B, G, Y = score[1], score[3], score[2], score[4]
    return 7*R + 5*B + 3*G + 2*Y


used = [False] * N
max_score = 0

def dfs(cnt: int, val_arr: list, col_arr: list):
    global max_score

    if cnt >= 3:
        curr_score = counting(val_arr, col_arr)
        max_score = max(curr_score, max_score)
        return
    
    for i in range(N):
        if used[i]:
            continue
        
        used[i] = True
        
        value = values[i]
        color = colors[i]
        for _ in range(4):
            new_val_field = rotate(value)
            new_col_field = rotate(color)
            value = new_val_field
            color = new_col_field
            
            for row in range(2):
                for col in range(2):
                    new_val_arr, new_col_arr = put(val_arr, col_arr, value, color, row, col)
                    dfs(cnt + 1, new_val_arr, new_col_arr)
        used[i] = False


dfs(0, val_arr, col_arr)
print(max_score)


# 2) 색상을 문자열형태 그대로 저장. (품질, 색상)로 배열 저장.
from sys import stdin


input = stdin.readline

N = int(input())

arr = [[(0, "W")] * 5 for _ in range(5)]
fields = []

for _ in range(N):
    value = [list(map(int, input().split())) for _ in range(4)]
    color = [list(input().rstrip().split()) for _ in range(4)]

    field = [[(value[i][j], color[i][j]) for j in range(4)] for i in range(4)]
    fields.append(field)


# 90º 회전 함수
def rotate(field: list) -> list:
    return [[field[3-j][i] for j in range(4)] for i in range(4)]


# 선택한 재료를 가마에 투입시키는 함수
def put(arr: list, field: list, x: int, y: int) -> list:
    new_arr = [line[:] for line in arr]

    for i in range(4):
        for j in range(4):
            val, col = arr[x+i][y+j]
            val += field[i][j][0]

            val = min(9, max(0, val))

            if field[i][j][1] != "W":
                col = field[i][j][1]

            new_arr[x+i][y+j] = (val, col)
    return new_arr


# 가마 점수 계산 함수
def counting(arr: list) -> int:
    R = B = G = Y = 0

    for i in range(5):
        for j in range(5):
            val, col = arr[i][j]
            if col == "R":
                R += val
            elif col == "B":
                B += val
            elif col == "G":
                G += val
            elif col == "Y":
                Y += val
    return 7*R + 5*B + 3*G + 2*Y


used = [False] * N
max_score = 0

def dfs(cnt: int, arr: list):
    global max_score

    if cnt >= 3:
        curr_score = counting(arr)
        max_score = max(curr_score, max_score)
        return
    
    for i in range(N):
        if used[i]:
            continue
        
        used[i] = True
        
        field = fields[i]

        for _ in range(4):
            field = rotate(field)

            for row in range(2):
                for col in range(2):
                    new_arr = put(arr, field, row, col)
                    dfs(cnt + 1, new_arr)
        used[i] = False


dfs(0, arr)
print(max_score)


# 3) 각 재료를 회전시킨 배열을 미리 저장
from sys import stdin


input = stdin.readline

N = int(input())

arr = [[(0, "W")] * 5 for _ in range(5)]
fields = []

for _ in range(N):
    value = [list(map(int, input().split())) for _ in range(4)]
    color = [list(input().rstrip().split()) for _ in range(4)]

    field = [[(value[i][j], color[i][j]) for j in range(4)] for i in range(4)]
    fields.append(field)


# 90º 회전 함수
def rotate(field: list) -> list:
    return [[field[3-j][i] for j in range(4)] for i in range(4)]


# 회전된 배열들을 저장할 딕셔너리
rotated = {}

for i in range(N):
    curr_field = fields[i]
    rotated[i] = []
    for _ in range(4):
        curr_field = rotate(curr_field)
        rotated[i].append(curr_field)


# 선택한 재료를 가마에 투입시키는 함수
def put(arr: list, field: list, x: int, y: int) -> list:
    new_arr = [line[:] for line in arr]

    for i in range(4):
        for j in range(4):
            val, col = arr[x+i][y+j]
            val += field[i][j][0]
            val = min(9, max(0, val))

            if field[i][j][1] != "W":
                col = field[i][j][1]

            new_arr[x+i][y+j] = (val, col)
    return new_arr


# 가마 점수 계산 함수
def counting(arr: list) -> int:
    R = B = G = Y = 0

    for i in range(5):
        for j in range(5):
            val, col = arr[i][j]
            if col == "R":
                R += val
            elif col == "B":
                B += val
            elif col == "G":
                G += val
            elif col == "Y":
                Y += val
    return 7*R + 5*B + 3*G + 2*Y


used = [False] * N
max_score = 0

def dfs(cnt: int, arr: list):
    global max_score

    if cnt >= 3:
        curr_score = counting(arr)
        max_score = max(curr_score, max_score)
        return
    
    for i in range(N):
        if used[i]:
            continue
        
        used[i] = True

        for field in rotated[i]:
            for row in range(2):
                for col in range(2):
                    new_arr = put(arr, field, row, col)
                    dfs(cnt + 1, new_arr)
        used[i] = False


dfs(0, arr)
print(max_score)
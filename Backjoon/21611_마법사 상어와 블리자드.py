# 문제집 - 0x0D강 - 시뮬레이션


# 문제: https://www.acmicpc.net/problem/21611

# 배열 돌리기4, 상어 중학교, 미세먼지 안녕! 등등... 과 비슷해보이지만 다름.
# 위 문제들처럼 빈공간을 찾아 땡기고 밀고 하다보면 머리 터짐.

# 메모리: 32412KB / 시간: 184ms
from sys import stdin


input = stdin.readline


def mapping(field: list) -> tuple[list, list]:
    """ (좌표) ↔ (구슬 순서) 를 맵핑시키고, 순서대로 1차원 리스트에 옮겨 담는 함수 """
    pos = [[0] * N for _ in range(N)]  # pos[i][j] = (i,j) 위치에 해당되는 구슬의 인덱스 번호(marbles[번호]로 매치시킬거임)
    marbles = [0] * (N*N)  # 구슬을 순서대로 담음 (나선형 방향대로)

    # ←, ↓, →, ↑ 순서로 돌아감
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]

    length = 1
    cnt = 1
    dir = 0  # 초기 방향은 좌
    x = y = N//2

    while cnt < N*N:
        for _ in range(2):  # 길이마다 두번씩 반복됨
            for _ in range(length):
                x += dx[dir]
                y += dy[dir]
                if 0 <= x < N and 0 <= y < N:
                    marbles[cnt] = field[x][y]
                    pos[x][y] = cnt
                    cnt += 1
            dir = (dir + 1) % 4  # 길이만큼 돌았으면 방향 바꾸기
        length += 1
    return marbles, pos


def blizard(d: int, s: int, pos: list, marbles: list) -> list:
    """ 블리자드 (얼음 파편 날리기) 시전 함수 """
    # ↑, ↓, ←, →
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    x = y = N//2
    for _ in range(s):
        x += dx[d]
        y += dy[d]

        if 0 <= x < N and 0 <= y < N:
            # 인덱스에 해당되는 구슬 폭파
            num = pos[x][y]
            marbles[num] = 0
    return marbles


def moving(marbles: list) -> list:
    """ 구슬 이동 함수 """
    new_marbles = [0] * (N*N)

    idx = 1
    for marble in marbles:
        if marble != 0:
            new_marbles[idx] = marble
            idx += 1
    return new_marbles


def bombing(marbles: list) -> list:
    while True:
        bomb = False

        i = 1
        while i < N*N:  # 0번째 구슬은 상어 자신. 유효한 인덱스 범위는 N*N-1까지임.
            j = i + 1
            while j < N*N and marbles[j] == marbles[i] and marbles[j] != 0:
                j += 1
            if (j - i) >= 4 and marbles[i] != 0:  # 위 조건에 부합되는 구슬은 (j-1)번째 구슬까지이므로...
                bomb = True
                score[marbles[i]] += (j - i)
                for k in range(i, j):
                    marbles[k] = 0
            i = j
        
        if not bomb:  # 폭파되지 않았다면 종료
            break

        marbles = moving(marbles)
    return marbles


def grouping(marbles: list) -> list:
    """ 구슬을 그룹화 한 뒤 재배열하는 함수 """
    new_marbles = [0] * (N*N)
    idx = 1  # new_marbles의 인덱스

    # 구슬의 갯수, 구슬의 번호 순으로 추가하기
    # i, j = 기존 marbles의 인덱스
    i = 1
    while i < N*N and marbles[i] != 0:
        j = i + 1
        while j < N*N and marbles[j] == marbles[i] and marbles[j] != 0:
            j += 1
        
        if idx < N*N:
            new_marbles[idx] = (j-i)
            idx += 1
        if idx < N*N:  # 구슬의 갯수를 추가한 뒤에도 칸이 남아있다면
            new_marbles[idx] = marbles[i]
            idx += 1
        
        i = j
    return new_marbles


N, M = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(N)]
score = [0, 0, 0, 0]
# 맵핑부터!
marbles, pos = mapping(field)

for _ in range(M):
    d, s = map(int, input().split())

    # 1-1. 블리자드 시전
    marbles = blizard(d-1, s, pos, marbles)
    # 1-2. 시전 후 구슬 이동
    marbles = moving(marbles)

    # 2. 구슬 폭발 + 이동
    marbles = bombing(marbles)

    # 3. 구슬 그룹핑 후 재배열
    marbles = grouping(marbles)


ret = score[1] + 2*score[2] + 3*score[3]
print(ret)
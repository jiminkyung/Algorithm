# 문제집 - 0x0D강 - 시뮬레이션


# 문제: https://www.acmicpc.net/problem/23290

# 단순 구현 문제.
# 3차원 리스트를 사용할까 하다가 defaultdict를 사용했는데 패착이었다...
# 또한 상어의 3칸 이동 경로를 구성할때, 나올 수 있는 경우의 수는 4*4*4 = 64개 뿐이므로,
# DFS보다 단순 3중 for문으로 구현하는게 낫다.

# 1) 딕셔너리 + DFS
# 메모리: 60684KB / 시간: 1196ms
from sys import stdin
from collections import defaultdict


input = stdin.readline

fish_dx = [0, -1, -1, -1, 0, 1, 1, 1]
fish_dy = [-1, -1, 0, 1, 1, 1, 0, -1]

shark_dx = [-1, 0, 1, 0]
shark_dy = [0, -1, 0, 1]

M, S = map(int, input().split())

# 일단 냄새와 상어 위치는 분리시켜야함.
fishes = defaultdict(list)  # [물고기 위치]: 방향

for _ in range(M):
    x, y, d = map(int, input().split())
    fishes[(x-1, y-1)].append(d-1)

sx, sy = map(int, input().split())
shark = (sx-1, sy-1)

smell = {}

def fish_moving(fishes):
    new_fishes = defaultdict(list)

    for pos, direction in fishes.items():
        x, y = pos
        for d in direction:
            can_move = False
            for i in range(8):
                nd = (d - i) % 8
                nx, ny = x + fish_dx[nd], y + fish_dy[nd]

                if 0 > nx or nx >= 4 or 0 > ny or ny >= 4:
                    continue

                if (nx, ny) != shark and (nx, ny) not in smell:
                    new_fishes[(nx, ny)].append(nd)
                    can_move = True
                    break
            if not can_move:
                new_fishes[(x, y)].append(d)
    return new_fishes


def shark_moving(fishes):
    max_fish = -1
    best_route = [0, 0, 0]

    def dfs(route, fish, x, y, visited):
        nonlocal max_fish

        if len(route) == 3:
            if max_fish < fish:
                best_route[0], best_route[1], best_route[2] = route[0], route[1], route[2]
                max_fish = fish
            elif max_fish == fish and route < best_route:
                best_route[0], best_route[1], best_route[2] = route[0], route[1], route[2]
            return
        
        for d in range(4):
            nx, ny = x + shark_dx[d], y + shark_dy[d]
            if 0 <= nx < 4 and 0 <= ny < 4:
                fish_cnt = 0
                is_new = (nx, ny) not in visited

                if is_new:
                    fish_cnt = len(fishes[(nx, ny)])
                    visited.add((nx, ny))

                dfs(route + [d], fish + fish_cnt, nx, ny, visited)

                if is_new:
                    visited.remove((nx, ny))
    
    dfs([], 0, shark[0], shark[1], set())
    return best_route


for turn in range(1, S+1):
    # 1. 물고기 복제 마법 뾰로롱~
    fish_copy = {k: v[:] for k, v in fishes.items()}  # 복제한 물고기의 좌표들은 따로 저장해둠

    # 2. 물고기들 이동
    fishes = fish_moving(fishes)

    # 3-1. 상어 3칸 이동경로 구하기
    best_route = shark_moving(fishes)

    # 3-2. 상어의 경로대로 물고기 냠냠...
    sx, sy = shark
    for d in best_route:
        nx, ny = sx + shark_dx[d], sy + shark_dy[d]
        if fishes[(nx, ny)]:
            smell[(nx, ny)] = turn
        del fishes[(nx, ny)]
        sx, sy = nx, ny
    
    shark = (sx, sy)  # 상어 위치 업데이트

    # 4. 두 턴 전에 남겼던 냄새 없애기
    smelled = []
    for pos, v in smell.items():
        if v == turn-2:
            smelled.append(pos)

    for pos in smelled:
        del smell[pos]
    
    # 5. 복제 마법 완료. 복제한 물고기도 추가시키기.
    for pos, directions in fish_copy.items():
        fishes[pos].extend(directions)

ret = 0

for v in fishes.values():
    ret += len(v)

print(ret)


# 2) 딕셔너리 + 3중for문
# => 똑같이 딕셔너리를 사용해서 큰 차이 없음ㅜ
# 메모리: 51096KB / 시간: 1192ms
from sys import stdin
from collections import defaultdict


input = stdin.readline

fish_dx = [0, -1, -1, -1, 0, 1, 1, 1]
fish_dy = [-1, -1, 0, 1, 1, 1, 0, -1]

shark_dx = [-1, 0, 1, 0]
shark_dy = [0, -1, 0, 1]

M, S = map(int, input().split())

fishes = defaultdict(list)  # [물고기 위치]: 방향

for _ in range(M):
    x, y, d = map(int, input().split())
    fishes[(x-1, y-1)].append(d-1)

sx, sy = map(int, input().split())
shark = (sx-1, sy-1)

smell = {}

def fish_moving(fishes):
    new_fishes = defaultdict(list)

    for pos, direction in fishes.items():
        x, y = pos
        for d in direction:
            can_move = False
            for i in range(8):
                nd = (d - i) % 8
                nx, ny = x + fish_dx[nd], y + fish_dy[nd]

                if 0 > nx or nx >= 4 or 0 > ny or ny >= 4:
                    continue

                if (nx, ny) != shark and (nx, ny) not in smell:
                    new_fishes[(nx, ny)].append(nd)
                    can_move = True
                    break
            if not can_move:
                new_fishes[(x, y)].append(d)
    return new_fishes


def shark_moving(fishes):
    max_fish = -1
    best_route = [0, 0, 0]

    for i in range(4):
        for j in range(4):
            for k in range(4):
                x, y = shark
                route = [i, j, k]
                visited = set()
                fish = 0
                can_move = True
                for r in route:
                    nx, ny = x + shark_dx[r], y + shark_dy[r]
                    if not (0 <= nx < 4 and 0 <= ny < 4):
                        can_move = False
                        break
                    if (nx, ny) not in visited:
                        visited.add((nx, ny))
                        fish += len(fishes[(nx, ny)])
                    x, y = nx, ny
                if not can_move:
                    continue
                if max_fish < fish:
                    max_fish = fish
                    best_route = [i, j, k]
                elif max_fish == fish and route < best_route:
                    best_route = [i, j, k]
    return best_route


for turn in range(1, S+1):
    # 1. 물고기 복제 마법 뾰로롱~
    fish_copy = {k: v[:] for k, v in fishes.items()}  # 복제한 물고기의 좌표들은 따로 저장해둠

    # 2. 물고기들 이동
    fishes = fish_moving(fishes)

    # 3-1. 상어 3칸 이동경로 구하기
    best_route = shark_moving(fishes)

    # 3-2. 상어의 경로대로 물고기 냠냠...
    sx, sy = shark
    for d in best_route:
        nx, ny = sx + shark_dx[d], sy + shark_dy[d]
        if fishes[(nx, ny)]:
            smell[(nx, ny)] = turn
        del fishes[(nx, ny)]
        sx, sy = nx, ny
    
    shark = (sx, sy)  # 상어 위치 업데이트

    # 4. 두 턴 전에 남겼던 냄새 없애기
    smelled = []
    for pos, v in smell.items():
        if v == turn-2:
            smelled.append(pos)

    for pos in smelled:
        del smell[pos]
    
    # 5. 복제 마법 완료. 복제한 물고기도 추가시키기.
    for pos, directions in fish_copy.items():
        fishes[pos].extend(directions)

ret = 0

for v in fishes.values():
    ret += len(v)

print(ret)


# 실행시간 1위인 코드. 3차원 리스트로 관리함! 머리를 쓰자...
# 👉 https://www.acmicpc.net/source/84850990
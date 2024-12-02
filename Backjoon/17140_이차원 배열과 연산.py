# 문제집 - 0x0D강 - 시뮬레이션


# 문제: https://www.acmicpc.net/problem/17140
# 메모리: 31120KB / 시간: 52ms
from sys import stdin


input = stdin.readline

r, c, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(3)]
time = 0

def R() -> list:
    new_arr = []
    max_len = 0

    for line in arr:
        line_set = set(line)

        tmp = [(l, line.count(l)) for l in line_set if l != 0]
        tmp.sort(key=lambda x: (x[1], x[0]))
        tmp = [item for sum_item in tmp for item in sum_item]
        if len(tmp) > 100:
            tmp = tmp[:100]
        new_arr.append(tmp)

        max_len = max(len(tmp), max_len)

    for i in range(len(arr)):
        new_arr[i] = new_arr[i] + [0] * (max_len - len(new_arr[i]))
    
    return new_arr


def C() -> list:
    # 행렬을 뒤집기 => 정렬 => 다시 뒤집어준 후 반환
    new_arr = []
    max_len = 0

    for line in map(list, zip(*arr)):
        line_set = set(line)

        tmp = [(l, line.count(l)) for l in line_set if l != 0]
        tmp.sort(key=lambda x: (x[1], x[0]))
        tmp = [item for sub_item in tmp for item in sub_item]
        new_arr.append(tmp)

        max_len = max(len(tmp), max_len)
    
    for i in range(len(arr[0])):
        new_arr[i] = new_arr[i] + [0] * (max_len - len(new_arr[i]))
    
    revert_arr = list(map(list, zip(*new_arr)))
    return revert_arr


while True:
    n, m = len(arr), len(arr[0])

    if n >= r and m >= c and arr[r-1][c-1] == k:
        print(time)
        break
    if time > 100:
        print(-1)
        break

    if n >= m:
        arr = R()
    else:
        arr = C()
    time += 1
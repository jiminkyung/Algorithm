# 문제집 - 0x0D강 - 시뮬레이션


# 문제: https://www.acmicpc.net/problem/17779

# 처음엔 5번 선거구 표시 후 1~4번 선거구를 한번에 채우는 방식을 사용했다.
# 하지만 범위로만 선거구를 구별하면 87%에서 틀림.
# 반례👉 https://www.acmicpc.net/board/view/152220
# 해결방법: 방향에 맞춰 선거구를 채우고, 도중에 경계선을 만나면 break.

# 1. 5번 선거구에 해당되는 구역을 수정해가며 실시간 카운트
# 메모리: 32412KB / 시간: 548ms
from sys import stdin


input = stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]


def dividing(x, y, d1, d2):
    field = [line[:] for line in arr]
    nums = [0] * 5  # 선거구의 인구 수

    # 경계선 먼저 체크
    for i in range(d1+1):  # 1, 4번 경계선
        nums[4] += field[x+i][y-i]
        nums[4] += field[x+d2+i][y+d2-i]
        field[x+i][y-i] = 0
        field[x+d2+i][y+d2-i] = 0
    for i in range(d2+1):  # 2, 3번 경계선
        nums[4] += field[x+i][y+i]
        nums[4] += field[x+d1+i][y-d1+i]
        field[x+i][y+i] = 0
        field[x+d1+i][y-d1+i] = 0

    # 5번 선거구 내부 체크
    for i in range(x+1, x+d1+d2):  # 경계선의 범위 x ~ x+d1+d2 기준.
        flag = False
        for j in range(N):
            if field[i][j] == 0:  # 경계선을 만나면 flag를 반전시킴.
                flag = not flag
                continue
            if flag:
                nums[4] += field[i][j]
                field[i][j] = 0

    # 경계선을 만나면 break 되도록 진행해야함.
    # 🚨즉, 5번 선거구의 왼쪽 부분은 왼쪽->오른쪽, 오른쪽 부분은 오른쪽->왼쪽 순서로 채워나가야한다.
    # 1번 선거구: 왼쪽 -> 오른쪽
    for r in range(x+d1):
        for c in range(y+1):
            if field[r][c] == 0:
                break
            nums[0] += field[r][c]

    # 2번 선거구: 오른쪽 -> 왼쪽
    for r in range(x+d2+1):
        for c in range(N-1, y, -1):
            if field[r][c] == 0:
                break
            nums[1] += field[r][c]

    # 3번 선거구: 왼쪽 -> 오른쪽
    for r in range(x+d1, N):
        for c in range(y-d1+d2):
            if field[r][c] == 0:
                break
            nums[2] += field[r][c]

    # 4번 선거구: 오른쪽 -> 왼쪽
    for r in range(x+d2+1, N):
        for c in range(N-1, y-d1+d2-1, -1):
            if field[r][c] == 0:
                break
            nums[3] += field[r][c]

    return max(nums) - min(nums)


min_diff = float("inf")

# x, y 범위값에 0-based 처리
for x in range(N-2):  # 1 <= x <= N-2
    for y in range(1, N-1):  # 2 <= y <= N-1
        for d1 in range(1, y+1):  # 1 <= d1 < y
            for d2 in range(1, N-y):  # 1 <= d2 < N-y+1
                if x + d1 + d2 >= N or y - d1 < 0 or y + d2 >= N:
                    continue

                min_diff = min(dividing(x, y, d1, d2), min_diff)
                if min_diff == 0:  # 차이가 0이면 프로그램 종료
                    print(0)
                    exit()

print(min_diff)


# 2. 5번 선거구를 구별할 리스트를 따로 생성 (이게 더 깔끔해보임)
# 메모리: 32412KB / 시간: 692ms
from sys import stdin


input = stdin.readline

N = int(input())
field = [list(map(int, input().split())) for _ in range(N)]


def dividing(x, y, d1, d2):
    nums = [0] * 5  # 선거구의 인구 수
    arr = [[0] * N for _ in range(N)]  # 5번 선거구 구별용

    # 경계선 먼저 채우기
    for i in range(d1+1):  # 1, 4번 경계선
        arr[x+i][y-i] = 5
        arr[x+d2+i][y+d2-i] = 5
    for i in range(d2+1):  # 2, 3번 경계선
        arr[x+i][y+i] = 5
        arr[x+d1+i][y-d1+i] = 5

    # 5번 선거구 내부 채우기
    for i in range(x+1, x+d1+d2):  # 경계선의 범위 x ~ x+d1+d2 기준.
        flag = False
        for j in range(N):
            if arr[i][j] == 5:  # 경계선을 만나면 flag를 반전시킴.
                flag = not flag
                continue
            if flag:
                arr[i][j] = 5

    # 경계선을 만나면 break 되도록 진행해야함.
    # 🚨즉, 5번 선거구의 왼쪽 부분은 왼쪽->오른쪽, 오른쪽 부분은 오른쪽->왼쪽 순서로 채워나가야한다.
    # 1번 선거구: 왼쪽 -> 오른쪽
    for r in range(x+d1):
        for c in range(y+1):
            if arr[r][c] == 5:
                break
            nums[0] += field[r][c]

    # 2번 선거구: 오른쪽 -> 왼쪽
    for r in range(x+d2+1):
        for c in range(N-1, y, -1):
            if arr[r][c] == 5:
                break
            nums[1] += field[r][c]

    # 3번 선거구: 왼쪽 -> 오른쪽
    for r in range(x+d1, N):
        for c in range(y-d1+d2):
            if arr[r][c] == 5:
                break
            nums[2] += field[r][c]

    # 4번 선거구: 오른쪽 -> 왼쪽
    for r in range(x+d2+1, N):
        for c in range(N-1, y-d1+d2-1, -1):
            if arr[r][c] == 5:
                break
            nums[3] += field[r][c]

    # 5번 선거구
    nums[4] = sum(field[i][j] for i in range(N) for j in range(N) if arr[i][j] == 5)

    return max(nums) - min(nums)


min_diff = float("inf")

# x, y 범위값에 0-based 처리
for x in range(N-2):  # 1 <= x <= N-2
    for y in range(1, N-1):  # 2 <= y <= N-1
        for d1 in range(1, y+1):  # 1 <= d1 < y
            for d2 in range(1, N-y):  # 1 <= d2 < N-y+1
                if x + d1 + d2 >= N or y - d1 < 0 or y + d2 >= N:
                    continue

                min_diff = min(dividing(x, y, d1, d2), min_diff)
                if min_diff == 0:  # 차이가 0이면 프로그램 종료
                    print(0)
                    exit()

print(min_diff)
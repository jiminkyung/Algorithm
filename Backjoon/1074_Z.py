# 문제집 - 0x0B - 재귀


# 문제: https://www.acmicpc.net/problem/1074

# 4사분면으로 나눴을때 r, c가 어느 영역에 속하는지 체크한 뒤 조건적으로 재귀를 돌려야한다.

# 첫번째 시도. 메모리초과.
# 2 ** N 만큼 리스트를 생성해줘야하므로 과부하가 걸린다.
# 리스트(배열)을 사용하지 않고 푸는 방법을 찾아봐야함.
from sys import stdin


N, r, c = map(int, stdin.readline().split())

arr = [[0] * (2 ** N) for _ in range(2 ** N)]
cnt = 0

def make_z(x, y, n):
    global cnt
    if n == 1: 
        for i in range(2):
            for j in range(2):
                arr[x+i][y+j] = cnt
                cnt += 1
        return
    
    m = n // 2
    make_z(x, y, m)
    make_z(x, y+n, m)
    make_z(x+n, y, m)
    make_z(x+n, y+n, m)

make_z(0, 0, 2 ** N)

print(arr[r][c])


# 두번째 시도. 시간초과다. 그리고 코드가 더럽다...
from sys import stdin


N, r, c = map(int, stdin.readline().split())

cnt = 0

def make_z(x, y, n):
    global cnt
    if n == 1: 
        for i in range(2):
            for j in range(2):
                if x+i == r and y+j == c:
                    print(cnt)
                    return
                cnt += 1
        return
    
    m = n // 2

    for dx, dy in ((0, 0), (0, n), (n, 0), (n, n)):
        nx, ny = dx + x, dy + y
        
        if r >= nx and c >= ny:
            make_z(nx, ny, m)
        else:
            cnt += n * n

make_z(0, 0, 2 ** N)


# ⭐ 정답 코드
# 메모리: 31120KB / 시간: 36ms
from sys import stdin


N, r, c = map(int, stdin.readline().split())

def make_z(n, r, c):
    if n == 0:
        return 0

    half = 2 ** (n-1)

    if r < half and c < half:  # 1사분면
        return make_z(n-1, r, c)
    elif r < half and c >= half:  # 2사분면
        return half * half + make_z(n-1, r, c-half)
    elif r >= half and c < half:  # 3사분면
        return 2 * half * half + make_z(n-1, r-half, c)
    else:  # 4사분면
        return 3 * half * half + make_z(n-1, r-half, c-half)

print(make_z(N, r, c))
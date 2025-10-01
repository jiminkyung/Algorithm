# 수학
# 구현
# 기하학


# 문제: https://www.acmicpc.net/problem/2477
# 무식하게 풀었건만. 훨씬 똑똑한 풀이가 있었다... 아래에 추가함.

# 1) 내 풀이
# 메모리: 32412KB / 시간: 36ms
from sys import stdin


input = stdin.readline

def main():
    K = int(input())
    # 차례대로 동서남북
    cnt = [0, 0, 0, 0]
    order = []

    for _ in range(6):
        d, l = map(int, input().split())

        cnt[d-1] += 1
        order.append((d-1, l))

    def check(flag: int) -> tuple[int, int, int, int]:
        lst = order * 3  # 해당 방향의 앞, 뒤를 확인해야하므로 안전성을 위해 3개를 이어 붙여줌
        w = h = -1
        mw = mh = -1
        # 남2동2
        if flag == 1:
            for i in range(6, 12):
                if lst[i][0] == 0 and lst[i-1][0] == 2 and lst[i+1][0] == 2:
                    mw, mh = lst[i][1], lst[i+1][1]
                
                if lst[i][0] == 1:
                    w = lst[i][1]
                if lst[i][0] == 3:
                    h = lst[i][1]
        # 북2동2
        elif flag == 2:
            for i in range(6, 12):
                if lst[i][0] == 0 and lst[i-1][0] == 3 and lst[i+1][0] == 3:
                    mw, mh = lst[i][1], lst[i-1][1]
                
                if lst[i][0] == 1:
                    w = lst[i][1]
                if lst[i][0] == 2:
                    h = lst[i][1]
        # 남2서2
        elif flag == 3:
            for i in range(6, 12):
                if lst[i][0] == 1 and lst[i-1][0] == 2 and lst[i+1][0] == 2:
                    mw, mh = lst[i][1], lst[i-1][1]
                
                if lst[i][0] == 0:
                    w = lst[i][1]
                if lst[i][0] == 3:
                    h = lst[i][1]
        # 북2서2
        else:
            for i in range(6, 12):
                if lst[i][0] == 1 and lst[i-1][0] == 3 and lst[i+1][0] == 3:
                    mw, mh = lst[i][1], lst[i+1][1]
                
                if lst[i][0] == 0:
                    w = lst[i][1]
                if lst[i][0] == 2:
                    h = lst[i][1]
        return w, h, mw, mh


    # 동 두번
    if cnt[0] == 2:
        # 남 2, 동 2
        if cnt[2] == 2:
            w, h, mw, mh = check(1)
        # 북 2, 동 2
        else:
            w, h, mw, mh = check(2)
    # 서 두번
    else:
        # 남 2, 서 2
        if cnt[2] == 2:
            w, h, mw, mh = check(3)
        # 북 2, 서 2
        else:
            w, h, mw, mh = check(4)
    
    total = w * h
    ret = total - mw * mh

    print(K * ret)


main()


# 2) 효율적인 풀이
# 출처👉 https://www.acmicpc.net/source/83075186
N = int(input())

arr = [list(map(int, input().split())) for _ in range(6)]

# 최대 길이
max_width = 0
max_width_idx = 0
# 최대 높이
max_height = 0
max_height_idx = 0

## 1, 2 가로 3, 4 세로
for t in range(6):
    if (arr[t][0] == 1 or arr[t][0] == 2):
        if max_width < arr[t][1]:
            max_width = arr[t][1]
            max_width_idx = t

    elif (arr[t][0] == 3 or arr[t][0] == 4):
        if max_height < arr[t][1]:
            max_height = arr[t][1]
            max_height_idx = t

big_square = max_width * max_height

# ⭐여기가 포인트임. 모든 모양에 상관없이 (max_width/width의 인덱스 + 3)번째는 작은 사각형의 세로/가로가 된다.
small_square = arr[(max_width_idx+3)%6][1] * arr[(max_height_idx+3)%6][1]

ans = (big_square - small_square) * N
print(ans)
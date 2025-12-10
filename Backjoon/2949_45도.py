# 구현
# 격자 그래프


# 문제: https://www.acmicpc.net/problem/2949

# 배열, 행렬 회전 문제. 구현 연습할때 다시 풀어볼만함.
# 메모리: 32412KB / 시간: 32ms
from sys import stdin


input = stdin.readline

def main():
    R, C = map(int, input().split())
    arr = [list(input().rstrip()) for _ in range(R)]
    angle = int(input())

    def rotate(arr: list, cnt: int) -> list:
        # cnt만큼 시계방향으로 90º 회전
        while cnt:
            R, C = len(arr), len(arr[0])
            
            new_arr = [[0] * R for _ in range(C)]
            for i in range(R):
                for j in range(C):
                    new_arr[j][R-1-i] = arr[i][j]
            
            arr = [line[:] for line in new_arr]
            cnt -= 1
        return arr
    

    # 직각에 맞게 돌릴 수 있을때까지 돌림 (90, 180, 270, 360)
    cnt = angle // 90
    arr = rotate(arr, cnt)
    R, C = len(arr), len(arr[0])

    # + 45º(대각선 방향)로 돌려야 할 경우
    if angle % 90:
        # s: 대각선의 각 줄. (i, j)의 합.
        # -> [00], [10, 01], [20, 11, 02]... 순으로 출력되는 패턴. 각 행렬 인덱스의 합은 대각선 줄 인덱스와 같음.
        for s in range(R+C - 1):
            # 공백
            space = " " * abs(s - (R-1)) if abs(s - (R-1)) else ""

            # s = i + j이고 j = s - i임.
            # 0 <= i <= R-1 and 0 <= j <= C-1 이어야 하는 상황.
            i_min = max(0, s - (C-1))
            i_max = min(s, R-1)

            line = []
            # 큰 행부터 내림차순으로
            for i in range(i_max, i_min-1, -1):
                j = s - i
                line.append(arr[i][j])
            line = " ".join(line)

            print(space + line)
    # 90º로 딱 떨어질경우 그냥 한줄씩 출력.
    else:
        for line in arr:
            print(*line, sep="")


main()
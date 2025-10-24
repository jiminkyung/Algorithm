# 구현


# 문제: https://www.acmicpc.net/problem/2669
# 메모리: 32412KB / 시간: 32ms
from sys import stdin


input = stdin.readline

def main():
    # 가능한 좌표는 0 ~ 100 까지이므로 배열의 크기를 101x101로 설정.
    arr = [[0] * 101 for _ in range(101)]
    cnt = 0

    for _ in range(4):
        y1, x1, y2, x2 = map(int, input().split())  # 행렬 기준으로 저장

        # 범위가 x1 ~ x2일때, x1과 x2 사이의 공간들이 선택됨.
        # arr[i][j]: arr[i][j] ~ arr[i][j+1] 사이의 공간 이라고 여기면,
        # x1 ~ x2의 실제 면적 = arr[x1][j] ~ arr[x2-1][j]인 셈.
        for i in range(x1, x2):
            for j in range(y1, y2):
                # 이미 칠해진 좌표면 넘어감
                if arr[i][j] == 1:
                    continue
                # 아니라면 칠한 후 카운트
                arr[i][j] = 1
                cnt += 1
    
    print(cnt)


main()
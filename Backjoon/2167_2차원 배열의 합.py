# 구현
# 누적 합


# 문제: https://www.acmicpc.net/board/view/140620

# 🗝️2차원 배열에서의 누적합을 사용해야 한다.
# 또는 각 행의 합을 구한 뒤, i ~ x행을 훑어내려가면서 계산하는 방법도 있음. 물론 2차원 누적합을 사용하는것보단 느리다.

# 1) 2차원 누적합 사용
# 메모리: 35480KB / 시간: 80ms
from sys import stdin


input = stdin.readline

def main():
    N, M = map(int, input().split())
    # 1-based로 맞추기 위해 0을 위, 왼쪽에 깔아둠
    arr = [[0] * (M+1)] + [[0] + list(map(int, input().split())) for _ in range(N)]
    
    # arr[i][j]: (1, 1)부터 (i, j)까지 직사각형의 합
    for i in range(1, N+1):
        for j in range(1, M+1):
            # 위쪽 직사각형 + 옆쪽 직사각형 - 위/옆 겹치는 직사각형
            arr[i][j] += arr[i-1][j] + arr[i][j-1] - arr[i-1][j-1]
    
    K = int(input())

    for _ in range(K):
        i, j, x, y = map(int, input().split())
        # 이제 (i, j) ~ (x, y) 구간의 직사각형 합을 구해줌.
        # (1, 1) ~ (x, y) 직사각형의 합 - 위쪽 직사각형 - 옆쪽 직사각형 + 위/옆 겹치는 직사각형
        ret = arr[x][y] - arr[i-1][y] - arr[x][j-1] + arr[i-1][j-1]

        print(ret)


main()


# 2) 행 별로 누적합 사용
# 메모리: 35480KB / 시간: 332ms
from sys import stdin


input = stdin.readline

def main():
    N, M = map(int, input().split())
    arr = [[0] * (M+1)] + [[0] + list(map(int, input().split())) for _ in range(N)]
    
    # 각 행의 누적합
    for i in range(1, N+1):
        for j in range(1, M+1):
            arr[i][j] += arr[i][j-1]
    
    K = int(input())

    for _ in range(K):
        i, j, x, y = map(int, input().split())
        ret = 0

        for row in range(i, x+1):
            ret += arr[row][y] - arr[row][j-1]
        
        print(ret)


main()
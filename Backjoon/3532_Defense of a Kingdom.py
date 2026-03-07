# 정렬
# 기하학


# 문제: https://www.acmicpc.net/problem/3532
# 메모리: 35824KB / 시간: 80ms
from sys import stdin


input = stdin.readline

def main():
    # 경계선을 포함해 불가능한 행/열을 모두 저장 -> 정렬 (오름/내림 상관 X)
    # 행/열별로 경계선 사이 텀의 길이를 구하고, 그 중 최댓값을 선택.
    w, h, n = map(int, input().split())

    # 경계선 추가
    # 격자의 범위는 (1 ~ w/h) 이므로 (0, w/h + 1) 값을 추가.
    x = [0, w+1]
    y = [0, h+1]

    for _ in range(n):
        i, j = map(int, input().split())
        x.append(i)
        y.append(j)
    
    x.sort()
    y.sort()

    max_x = max(x[i+1] - x[i] - 1 for i in range(n+1))
    max_y = max(y[i+1] - y[i] - 1 for i in range(n+1))

    # (최대 행 길이 * 최대 열 길이)
    print(max_x * max_y)


main()
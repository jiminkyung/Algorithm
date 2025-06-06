# 구현
# 시뮬레이션


# 문제: https://www.acmicpc.net/problem/1347

# 다시 풀어볼만한 문제
# 메모리: 32412KB / 시간: 40ms
from sys import stdin


input = stdin.readline

def main():
    """
    - 홍준이의 초기 위치 불분명
    - 홍준이가 적은 내용의 길이(이동거리)는 0 < x < 50

    즉, 미로의 최대 크기는 50x50 이다. 하지만 홍준이의 초기 위치를 모르는 상황이므로,
    충분히 큰 배열(100x100)을 만든 후 중앙(49, 49)을 시작 지점으로 임의 설정한다.
    이렇게 하면 어떤 방향으로 최대한 이동해도 배열 범위를 벗어나지 않음.

    지도 기록 후, 홍준이의 이동범위 중 최대/최소 좌표를 기준으로 배열 출력.
    """
    _ = int(input())
    arr = [["#"] * 100 for _ in range(100)]

    # 북, 동, 남, 서
    # 🚨왼쪽/오른쪽 회전은 홍준이 기준으로 판단해야함. 즉 3인칭 시점으로 봤을때는 L-> 반시계, R -> 시계 방향임.
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    d = 2  # 처음 방향은 남쪽

    # 배열의 시작점, 끝점 기록용
    min_x = min_y = max_x = max_y = 49    
    x = y = 49
    arr[x][y] = "."

    for move in input().rstrip():
        # 현재 방향 기준으로 전진
        if move == "F":
            x += dx[d]
            y += dy[d]
            arr[x][y] = "."
            
            # 경계값 갱신
            min_x = min(min_x, x)
            max_x = max(max_x, x)
            min_y = min(min_y, y)
            max_y = max(max_y, y)

        elif move == "L":  # 왼쪽 회전 (홍준 기준)
            d = (d - 1) % 4
        else:              # 오른쪽 회전
            d = (d + 1) % 4
    
    # 공백 없이 출력해야 함
    for x in range(min_x, max_x+1):
        print(*arr[x][min_y:max_y+1], sep="")


main()
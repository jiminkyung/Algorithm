# 구현
# 시뮬레이션


# 문제: https://www.acmicpc.net/problem/1491

# "나선" 키워드에 맞춰 계산식으로 풀어야 효율적임.
# 나처럼 단순 구현 풀이로도 통과는 되지만 엄청 비효율적이다...ㅜㅜ
# 나중에 다시 보면 좋을 풀이들도 아래에 추가함.

# 메모리: 227884KB / 시간: 5176ms
from sys import stdin


input = stdin.readline

def main():
    # 배열식으로 구성하기 위해 판 전체를 시계방향으로 90º 회전시킬거임.
    # 원래 M, N 순서로 주어지지만 판을 회전시키므로 N, M으로 입력받음.
    N, M = map(int, input().split())

    def moving() -> tuple:
        # 시작은 동쪽 -> 남쪽(시계), 턴은 왼쪽으로 -> 오른쪽으로(반시계)
        # 남 동 북 서
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        d = 0

        visited = [[False] * M for _ in range(N)]
        visited[0][0] = True
        x = y = 0
        cnt = N * M - 1

        while True:
            if cnt == 0:
                return (x, y)

            nx, ny = x + dx[d], y + dy[d]

            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                cnt -= 1
                visited[nx][ny] = True
                x, y = nx, ny
            else:
                d = (d + 1) % 4
    
    
    print(*moving())


main()


# 효율적인 코드 1
# 출처👉 https://www.acmicpc.net/source/52840748
n, m = map(int, input().split())

A = n  # 현재 진행 중인 행 이동 거리
S = n  # 현재 진행 중인 열 이동 거리

# x, y: 현재 위치 좌표 (초기 시작점은 (0, 0)의 왼쪽인 (-1, 0)에서 시작)
# => x가 -1인 상태에서 시작해야 n칸 이동했을 때 인덱스 범위를 벗어나지 않음.
# => x 갱신 후 S -= 1 을 수행하므로 y 좌표는 0부터 시작해도 됨. m-1을 더하는 꼴이기 때문.
x, y = -1, 0

P = 1  # 진행 방향 (1이면 오른쪽/위쪽, -1이면 왼쪽/아래쪽을 의미)

while True:
    # 1. 현재 방향(P)으로 행을 A칸 만큼 이동
    x += A * P
    S -= 1  # 열 이동 거리는 한 칸 줄어듦 (외곽 한 줄을 돌았으므로)
    if S == 0:
        break

    # 2. 현재 방향(P)으로 열을 S칸 만큼 이동
    y += S * P
    A -= 1  # 행 이동 거리도 한 칸 줄어듦
    if A == 0:
        break

    # 3. 방향 반전 (오른쪽↔왼쪽, 위쪽↔아래쪽)
    P *= -1

# 출력: 나선이 끝나는 좌표
print(x, y)


# 효율적인 풀이 2
# 나선 이동 패턴을 계산식으로 만든 풀이!
# 출처👉 https://www.acmicpc.net/source/91125271
n, m = map(int, input().split())

# 세로가 더 긴 경우: 위로 길게 뻗은 나선
if n > m:
    if m % 2 == 1:
        center = m // 2  # 나선의 층 수 (가로 기준)
        # 중심에서 세로로 (n - m)만큼 더 아래로 감겨 들어간다
        print(center + (n - m), center)
    else:
        center = m // 2
        # 짝수일 경우 중심이 2칸 → 왼쪽 아래 기준 좌표
        print(center - 1, center)

# 정사각형인 경우: 정확히 가운데
elif n == m:
    if m % 2 == 1:
        center = m // 2
        print(center, center)
    else:
        center = m // 2
        print(center - 1, center)

# 가로가 더 긴 경우: 옆으로 길게 뻗은 나선
else:
    if n % 2 == 1:
        center = n // 2
        # 중심에서 가로로 (m - n)만큼 더 오른쪽으로 감겨 들어감
        print(center, center + (m - n))
    else:
        center = n // 2
        print(center - 1, center)
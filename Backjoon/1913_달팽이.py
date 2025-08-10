# 구현


# 문제: https://www.acmicpc.net/problem/1913
# 메모리: 70982KB / 시간: 584ms
from sys import stdin


input = stdin.readline

def main():
    N = int(input())
    target = int(input())

    def snail(N: int, target: int) -> list | tuple[int, int]:
        # 북, 동, 남, 서 방향으로 회전
        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]

        arr = [[0] * N for _ in range(N)]
        tx = ty = 0  # target의 x, y 좌표

        x = y = N // 2
        size = cnt = 1
        d = 0

        while True:
            # d 방향으로 size만큼 전진. 각 size는 두번씩 반복됨.
            for _ in range(2):
                for _ in range(size):
                    if cnt == target:
                        tx, ty = x, y

                    # (x, y)에 번호 저장 후 이동
                    arr[x][y] = cnt
                    nx, ny = x + dx[d], y + dy[d]

                    if nx < 0 or nx >= N or ny < 0 or ny >= N:
                        return arr, (tx+1, ty+1)
                    
                    x, y = nx, ny
                    cnt += 1
                d = (d + 1) % 4
            size += 1
    

    arr, ret = snail(N, target)

    for line in arr:
        print(*line)
    
    print(*ret)


main()
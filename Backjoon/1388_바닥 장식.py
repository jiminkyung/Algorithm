# 구현
# 그래프 이론


# 문제: https://www.acmicpc.net/problem/1388
# 메모리: 32412KB / 시간: 36ms
from sys import stdin


input = stdin.readline

def main():
    N, M = map(int, input().split())
    arr = [input().rstrip() for _ in range(N)]
    visited = [[False] * M for _ in range(N)]

    cnt = 0

    for i in range(N):
        for j in range(M):
            if visited[i][j]:
                continue

            # 같은 무늬끼리 붙어있으면 한개로 취급
            if arr[i][j] == "-":
                cnt += 1
                tmp = j + 1
                while True:
                    if tmp < M and arr[i][tmp] == "-" and not visited[i][tmp]:
                        visited[i][tmp] = True
                        tmp += 1
                    else:
                        break
            else:
                cnt += 1
                tmp = i + 1
                while True:
                    if tmp < N and arr[tmp][j] == "|" and not visited[tmp][j]:
                        visited[tmp][j] = True
                        tmp += 1
                    else:
                        break
    print(cnt)


main()
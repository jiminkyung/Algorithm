# 구현
# 브루트포스 알고리즘


# 문제: https://www.acmicpc.net/problem/2508
# 메모리: 33432KB / 시간: 104ms
from sys import stdin


input = stdin.readline

def main():
    T = int(input())

    def check(R: int, C: int) -> int:
        cnt = 0
        arr = [input().rstrip() for _ in range(R)]
        visited = [[False] * C for _ in range(R)]

        for i in range(R):
            for j in range(C):
                if visited[i][j]:
                    continue

                # 사탕 알맹이일경우 체크
                if arr[i][j] == "o":
                    # ^v 체크
                    if 0 <= i-1 and i+1 < R and not visited[i-1][j] and not visited[i+1][j]:
                        if arr[i-1][j] == "v" and arr[i+1][j] == "^":
                            visited[i-1][j] = visited[i][j] = visited[i+1][j] = True
                            cnt += 1
                    # >< 체크
                    if 0 <= j-1 and j+1 < C and not visited[i][j-1] and not visited[i][j+1]:
                        if arr[i][j-1] == ">" and arr[i][j+1] == "<":
                            visited[i][j-1] = visited[i][j] = visited[i][j+1] = True
                            cnt += 1
        return cnt


    for _ in range(T):
        input()
        R, C = map(int, input().split())
        print(check(R, C))


main()
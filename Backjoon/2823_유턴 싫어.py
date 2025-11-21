# 그래프 이론


# 문제: https://www.acmicpc.net/problem/2823

# DFS로 푼 사람도 있고, 3차원 배열로 푼 사람도 있음.
# 그래프 연습할때 다른 방식으로 풀어봐도 괜찮을듯~ 다시 풀어볼만한 문제.

# 메모리: 32412KB / 시간: 36ms
from sys import stdin


input = stdin.readline

def main():
    R, C = map(int, input().split())
    field = [input().rstrip() for _ in range(R)]

    def bfs(R, C, field: list) -> int:
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]

        # 일단 길 아무곳이나 찾아서 시작점으로 지정.
        # 🚨무조건 (0, 0)으로 시작하면 안됨. (0, 0)이 막다른 길일 경우 제대로 판단하지 못함.
        for i in range(R):
            for j in range(C):
                if field[i][j] == ".":
                    curr = [(i, j)]
                    break
            else:
                continue
            break

        visited = [[False] * C for _ in range(R)]

        while curr:
            nxt = []
            for x, y in curr:
                # 현재 위치를 기준으로 동서남북 탐색. (x좌표, y좌표, 막힌 길인지 여부)
                directions = []
                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]
                    # 새 좌표가 격자를 벗어나거나, 막다른 길 이라면 True로 저장.
                    flag = not (0 <= nx < R and 0 <= ny < C) or field[nx][ny] == "X"
                    directions.append((nx, ny, flag))
                
                for i in range(4):
                    nx, ny, flag = directions[i]
                    # 막다른 방향 기준으로 양쪽을 체크.
                    # 만약 둘 다 막혀있다면 유턴을 해야 하므로 바로 1 return.
                    if flag:
                        if directions[i-1][2] and directions[(i+1)%4][2]:
                            return 1
                    else:
                        # 일반적인 길이고 아직 이동한 적 없다면, 방문처리 후 큐에 추가.
                        if not visited[nx][ny]:
                            visited[nx][ny] = True
                            nxt.append((nx, ny))
            curr = nxt
        return 0
    

    print(bfs(R, C, field))


main()
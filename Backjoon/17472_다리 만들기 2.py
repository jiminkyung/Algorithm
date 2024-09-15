# 최소 신장 트리


# 다시 풀어볼만한 문제.
# 메모리: 31120KB / 시간: 32ms

from sys import stdin


input = stdin.readline

def find_island(N, M, MAP: list):
    """
    지도에서 섬을 찾는 함수
    - visited: 방문한 좌표
    - islands: 섬들의 집합. 1부터 차례대로 저장. ex) [[섬1의 땅 좌표값들], [섬2의 땅 좌표값들]...]
    - num: 섬의 갯수
    """
    visited = [[False] * M for _ in range(N)]
    islands = []

    def dfs(x, y):
        """
        섬 하나의 땅 좌표값들을 탐색할 DFS 함수
        - island: 현재 섬에 해당하는 땅 좌표값들
        """
        stack = [(x, y)]
        visited[x][y] = True
        island = []

        while stack:
            curr_x, curr_y = stack.pop()
            island.append((curr_x, curr_y))

            for dx, dy in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
                nx, ny = curr_x + dx, curr_y + dy

                if 0 <= nx < N and 0 <= ny < M and MAP[nx][ny] and not visited[nx][ny]:
                    visited[nx][ny] = True
                    stack.append((nx, ny))
        return island
    
    num = 0
    for i in range(N):
        for j in range(M):
            if MAP[i][j] == 1 and not visited[i][j]:  # 현재 좌표가 땅이고, 방문하지 않은 상태라면
                islands.append(dfs(i, j))  # dfs를 실행 후 해당 섬의 좌표 리스트를 islands에 추가한다.
                num += 1
    
    return islands, num


def find_bridge(N, M, MAP, islands):
    """
    건설할 수 있는 다리를 찾는 함수
    - bridges: 다리의 좌표들을 저장하는 리스트
    """
    bridges = []

    def search(x, y, dx, dy, num):
        """
        특정 방향으로 다리를 놓을 수 있는지 확인하는 함수
        - x, y: 시작 좌표
        - dx, dy: 탐색 방향
        - num: 현재 섬의 번호
        - 반환값: (시작 섬 번호, 도착 섬 번호, 다리 길이) 또는 None
        """
        length = 0
        nx, ny = x + dx, y + dy
        while 0 <= nx < N and 0 <= ny < M:
            if MAP[nx][ny] == num:  # 같은 섬에 도달하면 종료
                return
            if MAP[nx][ny] != 0:  # 다른 섬에 도달하면, 길이가 2 이상임을 확인 후 반환
                return (num, MAP[nx][ny], length) if length >= 2 else None
            length += 1
            nx += dx
            ny += dy
    
    for n, island in enumerate(islands, start=1):
        for x, y in island:
            for dx, dy in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
                bridge = search(x, y, dx, dy, n)
                if bridge:
                    bridges.append(bridge)
    return bridges


def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def main():
    N, M = map(int, input().split())
    MAP = [list(map(int, input().split())) for _ in range(N)]

    islands, num = find_island(N, M, MAP)
    parent = list(range(num + 1))

    # 섬에 번호 부여하기
    for n, island in enumerate(islands, start=1):
        for x, y in island:
            MAP[x][y] = n
    
    # 탐색할 수 있는 다리 리스트를 받아오고 정렬한다.
    bridges = find_bridge(N, M, MAP, islands)
    bridges.sort(key=lambda x: x[2])

    # ret: 총 다리 길이, connected: 연결된 다리의 수
    ret = connected = 0

    for a, b, cost in bridges:
        fa, fb = find(parent, a), find(parent, b)

        if fa != fb:
            union(parent, fa, fb)
            ret += cost
            connected += 1

    # 모든 섬이 연결되었다면 ret을 반환하고, 아니라면 -1을 반환한다.
    print(ret if connected == num-1 else -1)

main()
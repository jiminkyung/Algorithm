# 문제집 - 0x09강 - BFS


# 문제: https://www.acmicpc.net/problem/3197

# 매번 BFS를 실행하면 시간초과!
# 호수 1번, 백조 1번 총 2번만 BFS가 실행되도록 설계해야함.
# => 호수용 큐 2개, 백조용 큐 2개를 생성하여 관리하면 됨.

# 백조/호수 각각 (현재 큐), (다음에 탐색할 큐)를 생성함.
# 백조 -> 호수를 가로지르며 가다가 얼음을 발견하면 다음날 이동할 큐에 삽입. 방문처리 해야함.
# 호수 -> 물로 이동중 얼음을 만나면 바로 물로 변환 후 다음날 큐에 삽입. 방문처리 필요 X.
# 어차피 호수 BFS에서는 얼음인 경우만 체크하므로 따로 visited를 생성해줄 필요 없음.

# 참고 게시글👉 https://www.acmicpc.net/board/view/65437

# 메모리: 138100KB / 시간: 3624ms
from sys import stdin
from collections import deque


input = stdin.readline

def main():
    def swan_bfs() -> bool:
        """ 백조가 서로 만날때까지 bfs 진행 """
        while swan_queue:
            x, y = swan_queue.popleft()

            if (x, y) == swans[1]:
                return True

            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]

                if not (0 <= nx < R and 0 <= ny < C) or swan_visited[nx][ny]:
                    continue

                swan_visited[nx][ny] = True

                # 만약 새로운 좌표가 물이라면 현재 큐에 추가,
                # 아니라면 다음 큐에 추가 후 다음 턴에서 이동 시도
                if lake[nx][ny] == ".":
                    swan_queue.append((nx, ny))
                else:
                    swan_nxt.append((nx, ny))
        return False

    def lake_bfs():
        """ 물에 닿은 얼음들 녹이기 """
        while water_queue:
            x, y = water_queue.popleft()

            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]

                # 만약 새로운 좌표가 얼음이라면 다음 큐에 삽입
                if 0 <= nx < R and 0 <= ny < C and lake[nx][ny] == "X":
                    lake[nx][ny] = "."
                    water_nxt.append((nx, ny))


    R, C = map(int, input().split())
    lake = []
    swans = []

    water_queue = deque()
    water_nxt = deque()

    for i in range(R):
        line = list(input().rstrip())
        lake.append(line)
        for j in range(C):
            # 백조 좌표값 저장 후 물로 바꿈
            if line[j] == "L":
                swans.append((i, j))
                line[j] = "."
            if line[j] == ".":
                water_queue.append((i, j))
    
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    swan_queue = deque([swans[0]])
    swan_nxt = deque()
    # 백조가 방문한 좌표들을 기록
    # => lake_bfs의 경우 좌표값이 물이라면 큐 추가 없이 넘어가지만, swan_bfs는 물일 경우와 얼음일 경우 모두 큐 처리를 해야하기때문.
    swan_visited = [[False] * C for _ in range(R)]
    swan_visited[swans[0][0]][swans[0][1]] = True

    day = 0
    
    while True:
        if swan_bfs():
            break

        lake_bfs()

        swan_queue = swan_nxt
        swan_nxt = deque()

        water_queue = water_nxt
        water_nxt = deque()

        day += 1
    
    print(day)


main()
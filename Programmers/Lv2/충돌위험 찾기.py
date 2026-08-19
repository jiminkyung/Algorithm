# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/340211


def solution(points: list[list[int]], routes: list[list[int]]) -> int:
    # crashes[(x, y, t)]: t시간에 (x, y)좌표에 위치해있던 로봇의 수
    crashes = {}


    def bfs(num: int):
        nonlocal crashes

        # 🚨 출발할 때 충돌하는 경우도 있으므로, 시작 위치도 체크해놔야 함.
        t = 0
        x, y = points[routes[num][0] - 1]
        crashes[(x, y, t)] = crashes.get((x, y, t), 0) + 1

        for nxt in range(1, len(routes[num])):
            # routes[i][j]: i번 로봇이 j번째로 방문할 포인트 번호
            r, c = points[routes[num][nxt] - 1]

            # 행 이동이 열 이동보다 우선되어야 함. 한칸씩 이동.
            if x > r:
                for i in range(x-1, r-1, -1):
                    t += 1
                    crashes[(i, y, t)] = crashes.get((i, y, t), 0) + 1
            elif x < r:
                for i in range(x+1, r+1):
                    t += 1
                    crashes[(i, y, t)] = crashes.get((i, y, t), 0) + 1
            
            if y > c:
                for i in range(y-1, c-1, -1):
                    t += 1
                    crashes[(r, i, t)] = crashes.get((r, i, t), 0) + 1
            elif y < c:
                for i in range(y+1, c+1):
                    t += 1
                    crashes[(r, i, t)] = crashes.get((r, i, t), 0) + 1
            
            # 새 좌표로 갱신
            x, y = r, c
    

    # 로봇들을 하나씩 실행하여 crashes 갱신
    for i in range(len(routes)):
        bfs(i)
    
    # 값이 2 이상인경우만 체크
    ret = sum(1 for val in crashes.values() if val > 1)
    return ret
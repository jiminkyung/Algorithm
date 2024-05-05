"""
양방향 고려((x, y, nx, ny), (nx, ny, x, y))를 해주지 않으면 TC 8번부터 통과 X.
문제에서는 "처음 걷는 길"을 구하라고 말한다.
예를들어, dirs가 "UDUD"로 주어질 경우 정답값은 1이 되어야 한다.
하지만 (x, y, nx, ny)로만 저장하면,
1. "U" -> (0, 0, 0, 1)
2. "D" -> (0, 1, 0, 0)
3, 4는 1, 2와 같음
즉 2를 반환하게 되므로 오답이다. 양방향 저장 후 2로 나누어야 알맞은 답을 뱉어낸다.
"""


# 방향(경로)를 고려하지 않음.
def solution(dirs):
    directions = {"U": (0, 1), "D": (0, -1), "L": (-1, 0), "R": (1, 0)}
    path = [(0, 0)]

    for dir in dirs:
        moves = (path[-1][0] + directions[dir][0], path[-1][1] + directions[dir][1])
        if moves[0] < -5 or moves[0] > 5 or moves[1] < -5 or moves[1] > 5:
            continue
        path.append(moves)
    return len(set(path)) - 1

# AI를 통해 얻은 정답 코드.
def solution(dirs):
    directions = {"U": (0, 1), "D": (0, -1), "L": (-1, 0), "R": (1, 0)}
    visited = set()
    x, y = 0, 0

    for dir in dirs:
        nx, ny = x + directions[dir][0], y + directions[dir][1]
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            visited.add((x, y, nx, ny))
            visited.add((nx, ny, x, y))
            x, y = nx, ny

    return len(visited) // 2
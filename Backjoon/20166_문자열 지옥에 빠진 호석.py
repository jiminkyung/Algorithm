# 문제집 - 0x15강 - 해시


# 문제: https://www.acmicpc.net/problem/20166

# 해시 문제 그 자체다.
# 각 칸에서 시작할 수 있는 문자열을 모두 탐색한 뒤 parts에 카운트한다.
# 신이 좋아하는 문자열이 parts에 있다면 카운트했던 값을 출력하고, 없다면 0을 출력.

# 메모리: 53232KB / 시간: 940ms
from sys import stdin


input = stdin.readline

N, M, K = map(int, input().split())
field = [input().rstrip() for _ in range(N)]
words = [input().rstrip() for _ in range(K)]

parts = {}

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]


def dfs(x, y, depth, word: str):
    if depth > 5:  # 문자열은 최대 5글자
        return
    
    # if word in words 조건을 넣으면 시간초과.
    parts[word] = parts.get(word, 0) + 1

    for i in range(8):
        nx = (x + dx[i]) % N
        ny = (y + dy[i]) % M

        dfs(nx, ny, depth+1, word + field[nx][ny])


for i in range(N):
    for j in range(M):
        dfs(i, j, 1, field[i][j])

for word in words:
    print(parts.get(word, 0))
# 동적 계획법 3


# 문제: https://www.acmicpc.net/problem/1311
# (PyPy3) 메모리: 118788KB / 시간: 820ms
from sys import stdin


input = stdin.readline
INF = int(1e9)

N = int(input())
D = [list(map(int, input().split())) for _ in range(N)]

dp = [INF] * (1 << N)  # 경우의 수가 000~111까지 8개이므로 1 << 3 => 8
dp[0] = 0

for i in range(1 << N):
    x = bin(i).count("1")

    for j in range(N):
        if not (i & (1 << j)):  # 이미 선택된 일이 아니라면
            nxt = i | (1 << j)
            dp[nxt] = min(dp[nxt], dp[i] + D[x][j])

print(dp[(1 << N) - 1])


# 아래는 Python3로 통과되는 코드다. 재귀를 사용.
# 출처: https://ji-gwang.tistory.com/446
# 메모리: 72080KB / 시간: 4796ms
import sys

input = sys.stdin.readline


def dfs(row, visit):
    if row == N:
        return 0

    if visited[visit] != -1:
        return visited[visit]

    ret = 1000000000
    for i in range(N):
        if (visit & (1 << i)) != 0:  # 특정 비트가 켜저있다면
            continue

        ret = min(ret, dfs(row + 1, (visit | (1 << i))) + tasks[row][i])

    visited[visit] = ret

    return visited[visit]


N = int(input())
tasks = [list(map(int, input().split())) for _ in range(N)]

visited = [-1] * (1 << N)
print(dfs(0, 0))


# 실행시간 48ms인 코드. Hungarian 알고리즘을 사용함.
from sys import stdin
from itertools import product

input = stdin.readline

N = int(input())
table = [list(map(int, input().split())) for _ in range(N)]


def hungarian(table):
    N = len(table)
    match_x, match_y = [None] * N, [None] * N
    label_x, label_y = list(map(max, table)), [0] * N
    is_free_x, is_free_y = (lambda x: match_x[x] == None), (
        lambda y: match_y[y] == None
    )
    gap = lambda i, j: label_x[i] + label_y[j] - table[i][j]

    while None in match_x:
        tree_x, tree_y = [None] * N, [None] * N
        S, T = [False] * N, [False] * N

        u = next(filter(is_free_x, range(N)))
        S[u] = True
        slack, slack_x = [gap(u, j) for j in range(N)], [u] * N

        while True:
            try:
                y = next(filter(lambda j: (slack[j] == 0) and (not T[j]), range(N)))

            except:
                min_gap = min(v for v, b in zip(slack, T) if not b)
                for i in range(N):
                    label_x[i] -= min_gap * int(S[i])
                    label_y[i] += min_gap * int(T[i])
                    slack[i] -= min_gap * int(not T[i])

            else:
                if is_free_y(y):
                    tree_y[y] = slack_x[y]
                    while y != None:
                        x = tree_y[y]
                        match_y[y], match_x[x], y = x, y, match_x[x]
                    break

                else:
                    z = match_y[y]
                    tree_x[z], tree_y[y] = y, slack_x[y]
                    S[z], T[y] = True, True
                    for i in range(N):
                        slack[i], slack_x[i] = min(
                            (gap(z, i), z), (slack[i], slack_x[i])
                        )

    return list(enumerate(match_x)), sum(label_x) + sum(label_y)


for i, j in product(range(N), repeat=2):
    table[i][j] *= -1

_, ans = hungarian(table)

print(-ans)
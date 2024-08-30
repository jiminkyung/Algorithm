# 동적 계획법과 최단거리 역추적
# https://www.acmicpc.net/problem/13913


# 이전 숨바꼭질 문제도 BFS문제였어서 비슷했다. 기존 문제에 역추적만 추가한 느낌이다.
# 메모리: 48064KB / 시간: 112ms

from collections import deque


def bfs(start, end):
    dp = [0] * 100001  # dp[i] = i까지 도달하는데에 걸리는 시간
    path = [0] * 100001

    queue = deque([start])
    while queue:
        curr = queue.popleft()

        if curr == end:
            return dp[curr], path

        for i in (curr+1, curr-1, 2*curr):  # 모두 1초가 소요되므로 우선순위를 따질 필요 X
            if 0 <= i <= 100000 and not dp[i]:
                queue.append(i)
                dp[i] = dp[curr] + 1
                path[i] = curr


N, K = map(int, input().split())
dis, path = bfs(N, K)
path_ret = []
tmp = K

for _ in range(dis + 1):  # 걸리는 시간만큼 반복
    path_ret.append(tmp)
    tmp = path[tmp]

path_ret.reverse()

print(dis)
print(" ".join(map(str, path_ret)))
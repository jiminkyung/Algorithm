# 동적 계획법 3


# 문제: https://www.acmicpc.net/problem/2098
# == Traveling Salesman problem (TSP)
# 메모리: 46540KB / 시간: 940ms
import sys


sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def dfs(start, visit):
    # 모든 도시를 방문했을때, 출발지로 가는 경로가 있다면 반환.
    if visit == (1 << N) - 1:  
        if W[start][0] != 0:
            return W[start][0]
        else:
            return int(1e9)

    if visited[start][visit] != -1:
        return visited[start][visit]
    
    ret = int(1e9)
    for i in range(N):
        if (visit & (1 << i)) != 0 or W[start][i] == 0:
            continue
        # i번 도시를 방문하지 않았고, start -> i로 가는 경로가 있다면
        ret = min(ret, dfs(i, visit | (1 << i)) + W[start][i])
    
    visited[start][visit] = ret
    return ret

N = int(input())
W = [list(map(int, input().split())) for _ in range(N)]

# visited[i][j] = 도시 i에서 j로 가는 비용
visited = [[-1] * (1 << N) for _ in range(N)]
print(dfs(0, 1))
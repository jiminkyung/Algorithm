# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/72413


def solution(n, s, a, b, fares: list[list[int, int, int]]) -> int:
    INF = int(1e9)
    graph = [[INF if i != j else 0 for j in range(n)] for i in range(n)]

    for u, v, w in fares:
        graph[u-1][v-1] = graph[v-1][u-1] = w
    
    # 플로이드 워셜로 풀어봄.
    # mid 지점까지 합승하고, 그 후 각자 도착지로 간다고 했을 때,
    # (s -> mid) + (mid -> a) + (mid -> b) 가 총 택시 요금임.
    # mid가 s일수도 있고, a일수도 b일수도 있으므로 모든 경우를 확인할 수 있음.
    # 만약 b와 a의 경로가 겹치거나, 따로 가는게 낫다면? 위에 적은대로 mid는 s, a, b 모두 가능하므로 확인 가능.
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if graph[i][k] + graph[k][j] < graph[i][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]
    
    min_cost = INF

    s -= 1
    a -= 1
    b -= 1

    for mid in range(n):
        # 출발노드 -> 합승노드 + 합승노드 -> a + 합승노드 -> b
        cost = graph[s][mid] + graph[mid][a] + graph[mid][b]

        if cost < min_cost:
            min_cost = cost
    
    return min_cost
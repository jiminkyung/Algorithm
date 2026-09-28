# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/49191


# 플로이드 워셜을 활용해서 풀이
def solution(n: int, results: list[list[int, int]]) -> int:
    graph = [[False if i != j else True for j in range(n)] for i in range(n)]

    # graph[i][j]: i가 j보다 강한지 판별
    for a, b in results:
        graph[a-1][b-1] = True
    
    # 플로이드 워셜로 직접 경기하지 않은 선수들 사이의 간접적인 승패 관계까지 모두 구함.
    # i -> k, k -> j 라면 i -> j 인것을 알 수 있음.
    for k in range(n):
        for i in range(n):
            for j in range(n):
                graph[i][j] = graph[i][j] or (graph[i][k] and graph[k][j])
    
    total = 0

    for i in range(n):
        # i와 j 중 어느 한쪽이라도 다른 쪽보다 강하다는 것을 알고 있으면, 두 선수의 상대적인 순위를 알 수 있음.
        cnt = sum(graph[i][j] or graph[j][i] for j in range(n))

        # i가 모든 선수에 대해 관계를 알 수 있으면 순위 결정 가능.
        if cnt == n:
            total += 1
    
    return total
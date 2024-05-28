# 그래프 관련 문제. 차라리 답을 보고 공부하는게 낫겠다 싶어 찾아봤다. 함수마다 필요한 정보는 주석으로 첨부.

def create_graph(n, wires):
    """
    전선 정보를 바탕으로 그래프를 생성하는 함수

    n: 송전탑의 개수
    wires: 전선 정보를 담은 2차원 리스트, 각 전선 정보는 [v1, v2] 형태로 주어지며 v1과 v2는 연결된 두 송전탑의 번호를 나타냄

    그래프는 무방향 그래프로 표현되며 인접 리스트를 사용하여 생성
    송전탑의 번호는 1부터 시작하므로 인덱스 0은 사용하지 않음
    """
    graph = [[] for _ in range(n + 1)]
    for v1, v2 in wires:
        graph[v1].append(v2)
        graph[v2].append(v1)
    return graph

def dfs(graph, start, visited):
    """
    DFS 탐색을 수행하여 연결된 송전탑의 개수를 세는 함수

    graph: 그래프 정보를 담은 2차원 리스트
    start: 탐색을 시작할 송전탑의 번호
    visited: 송전탑의 방문 여부를 나타내는 리스트, visited[i]는 i번 송전탑의 방문 여부를 나타내며 초기값은 모두 False로 설정됨

    DFS 탐색을 사용하여 연결된 송전탑 탐색
    스택을 사용하여 DFS 구현
    방문한 송전탑의 개수를 count 변수에 저장하여 반환
    """
    stack = [start]
    count = 0
    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = True
            count += 1
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    stack.append(neighbor)
    return count

def solution(n, wires):
    """
    전력망을 최적으로 분할하여 두 네트워크의 송전탑 개수 차이의 최솟값을 구하는 함수

    n: 송전탑의 개수
    wires: 전선 정보를 담은 2차원 리스트

    하나의 전선을 끊어서 두 개의 네트워크로 분할
    각 네트워크의 송전탑 개수 차이를 최소화하는 것이 목표
    모든 전선에 대해 하나씩 제거해보면서 송전탑 개수 차이 계산
    최솟값을 찾아 반환

    문제 해결에 필요한 개념: 그래프 이론, 트리 구조, DFS 탐색, 브루트포스 알고리즘
    """
    answer = float("inf")

    for i in range(len(wires)):
        # 그래프 생성
        graph = create_graph(n, wires[:i] + wires[i + 1 :])

        # 첫 번째 송전탑에서 시작해서 탐색
        visited = [False] * (n + 1)
        count = dfs(graph, 1, visited)

        # 두 네트워크의 송전탑 개수 차이 계산
        diff = abs(count - (n - count))
        answer = min(answer, diff)

    return answer
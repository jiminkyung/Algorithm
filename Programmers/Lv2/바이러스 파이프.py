# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/468373


from collections import deque


def solution(n, infection, edges: list[list[int]], k) -> int:
    graph = [[-1] * n for _ in range(n)]

    # 파이프 타입 저장
    for x, y, type in edges:
        graph[x-1][y-1] = type
        graph[y-1][x-1] = type
    

    def dfs(visited: list[bool], prev: int, k: int) -> int:
        """
        백트래킹으로 경우의 수 탐색.
        visited[i]: i번째 노드의 감염 유무
        prev: 이전에 선택한 파이프
        k: 남은 개폐횟수
        """
        if k == 0:
            cnt = sum(visited)
            return cnt
        
        max_cnt = 0

        for pipe in range(1, 4):
            if pipe == prev:  # 이전에 선택한 파이프는 쓰루
                continue

            node = []  # 새로 감염시킨 노드들
            queue = deque()

            for x in range(n):
                if visited[x]:
                    queue.append(x)
            
            # 기존에 감염된 노드와 파이프로 연결된 노드들을 모두 감염 처리.
            while queue:
                x = queue.popleft()

                for y in range(n):
                    if graph[x][y] == pipe and not visited[y]:
                        visited[y] = True
                        node.append(y)
                        queue.append(y)
            
            max_cnt = max(max_cnt, dfs(visited, pipe, k-1))

            # 새로 감염시켰던 노드들 복구
            for y in node:
                visited[y] = False
        
        return max_cnt
    

    visited = [False] * n
    visited[infection-1] = True  # 최초 감염 노드 체크

    ret = dfs(visited, 0, k)
    return ret
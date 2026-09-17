# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/49189


# 단순 BFS 문제
def solution(n: int, edge: list[list[int, int]]) -> int:
    graph = [[] for _ in range(n)]

    for a, b in edge:
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)
    

    def bfs():
        # visited[x]: x노드까지의 최단거리
        visited = [0] * n
        visited[0] = -1

        curr = [(0, 0)]

        while curr:
            nxt = []

            for node, dist in curr:
                for nxt_node in graph[node]:
                    # 아직 방문하지 않은 노드일경우, 현재 거리 + 1 값을 visited에 저장 후 큐에 추가.
                    if visited[nxt_node] == 0:
                        visited[nxt_node] = dist + 1
                        nxt.append((nxt_node, dist + 1))
            
            curr = nxt[:]
        
        # 가장 먼 거리를 구하고 해당 거리만큼 떨어져있는 노드들의 갯수를 구한다.
        max_dist = max(visited)
        ret = sum(1 for dist in visited if dist == max_dist)
        return ret
    
    
    return bfs()
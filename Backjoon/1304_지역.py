# 위상 정렬
# 너비 우선 탐색 (BFS)
# 브루트포스 알고리즘


# 문제: https://www.acmicpc.net/problem/1304

"""
고속도로는 1 -> 2 -> 3 -> ... -> N 이렇게 순서대로 방향 구성이 되어있음.
=> A -> B -> C도 A -> C 경로에 포함됨. 직통으로 가는 경로만 가능 경로가 아님

🚨 따라서 지역을 나눌때 순서대로 나눠줘야한다.
- [1, 2, 3, 4, 5, 6] -> [1, 2], [3, 4], [5, 6] 이런식으로.
- 만약 [1, 3], [2, 6], [4, 5] 처럼 섞이면 1 -> 2 가능, 2 -> 3 가능이므로 단방향 조건에 어긋난다.
- 위 조건대로 지역을 나눈 후, 위상 정렬로 단방향을 충족하는지(사이클이 없는지) 체크.
- 최대한 많이 쪼개야 유리하니까 N부터 1까지 역순으로 순회한다.
"""

# 1) BFS로 위상정렬
# 메모리: 34984KB / 시간: 64ms
from sys import stdin
from collections import deque


input = stdin.readline

def main():
    N, M = map(int, input().split())
    graph = [[i+1] for i in range(N-1)]
    graph.append([])  # N번 도시 추가

    for _ in range(M):
        S, E = map(int, input().split())
        graph[S-1].append(E-1)

    
    def DAG(city: list, cnt: int) -> bool:
        in_degree = [0] * cnt

        for s_city in range(cnt):
            for e_city in city[s_city]:
                in_degree[e_city] += 1
        
        queue = deque([i for i in range(cnt) if in_degree[i] == 0])
        visited = 0

        while queue:
            curr = queue.popleft()
            visited += 1
            
            for nxt in city[curr]:
                in_degree[nxt] -= 1
                if in_degree[nxt] == 0:
                    queue.append(nxt)
        
        return visited == cnt  # 사이클이 없다면 visited = 지역갯수 만족으로 True, 존재한다면 False
    

    # cnt: 나눌 지역의 수
    # size: 한 지역당 도시의 수
    for cnt in range(N, 0, -1):
        if N % cnt != 0:
            continue

        # city[x]: x 지역에서 갈 수 있는 지역들
        city = [[] for _ in range(cnt)]
        size = N // cnt

        # 모든 지역은 연속된 수열로 구성되어 있어야 함.
        # => (도시 번호) // (한 지역을 몇개의 도시로 구성할것인지) 로 지역 번호를 찾는다.
        # 위에서 0-based 처리를 해줬으므로 그냥 나누어줘도 됨.
        # ex) N = 9, size = 3일때 => 도시 3는 2 // 3 = 0번지역, 도시 4은 3 // 3 = 1번지역에 해당됨.
        for s in range(N):
            s_city = s // size
            for e in graph[s]:
                e_city = e // size
                if s_city != e_city:
                    city[s_city].append(e_city)
        
        # 모든 지역이 단방향이라면 출력
        if DAG(city, cnt):
            print(cnt)
            break


main()


# 2) DFS로 위상정렬
# 메모리: 34984KB / 시간: 60ms
from sys import stdin


input = stdin.readline

def main():
    N, M = map(int, input().split())
    graph = [[i+1] for i in range(N-1)]
    graph.append([])  # N번 도시 추가

    for _ in range(M):
        S, E = map(int, input().split())
        graph[S-1].append(E-1)


    def dfs(city: list, start: int) -> bool:
        """ 사이클이 존재하면 False 반환 """
        stack = [start]

        while stack:
            curr = stack[-1]

            if visited[curr] == 0:
                visited[curr] = 1
                for nxt in city[curr]:
                    if visited[nxt] == 0:
                        stack.append(nxt)
                    elif visited[nxt] == 1:
                        return False
            else:
                visited[curr] = 2
                stack.pop()
        return True


    # cnt: 나눌 지역의 수
    # size: 한 지역당 도시의 수
    for cnt in range(N, 0, -1):
        if N % cnt != 0:
            continue

        # city[x]: x 지역에서 갈 수 있는 지역들
        city = [[] for _ in range(cnt)]
        size = N // cnt

        # 모든 지역은 연속된 수열로 구성되어 있어야 함.
        # => (도시 번호) // (한 지역을 몇개의 도시로 구성할것인지) 로 지역 번호를 찾는다.
        # 위에서 0-based 처리를 해줬으므로 그냥 나누어줘도 됨.
        # ex) N = 9, size = 3일때 => 도시 3는 2 // 3 = 0번지역, 도시 4은 3 // 3 = 1번지역에 해당됨.
        for s in range(N):
            s_city = s // size
            for e in graph[s]:
                e_city = e // size
                if s_city != e_city:
                    city[s_city].append(e_city)
        
        visited = [0] * cnt
        has_cycle = False

        for i in range(cnt):
            if visited[i] != 0:
                continue
            if not dfs(city, i):
                has_cycle = True
                break
        
        # 모든 지역이 단방향이라면 출력
        if not has_cycle:
            print(cnt)
            break


main()
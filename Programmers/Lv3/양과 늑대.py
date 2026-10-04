# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/92343


# 그래프 문제
def solution(info: list[int], edges: list[list[int, int]]) -> int:
    N = len(info)
    graph = [[] for _ in range(N)]

    # graph[a]: [a의 자식노드들]
    for a, b in edges:
        graph[a].append(b)
    
    # 모든 노드를 방문해야 하는건 X
    # -> 따라서 중간마다 양의 수를 확인해야 함
    def dfs(s: int, w: int, candidates: list[int]):
        """
        어떤 노드 x에서 갈 수 있는 노드 = x의 자식노드들 이므로,
        a -> b -> c 순서로 노드를 방문했을 시 다음으로 방문할 수 있는 후보지는 [a, b, c의 자식노드들] 이다.

        따라서 후보지 candidates 중 하나를 다음 노드로 지정,
        candidates에서 해당 노드를 제외한 나머지 노드들 + 해당 노드의 자식들 을 새로운 candidates로 갱신하여 dfs한다.
        """

        # 늑대의 수가 양 이상이라면 멈춤
        if s <= w:
            return 0
        
        max_cnt = s
        
        for i in range(len(candidates)):
            # 새로운 candidates 생성
            nxt = candidates[i]
            new_candidates = candidates[:i] + candidates[i+1:] + graph[nxt]

            # nxt가 양일 경우/늑대일 경우를 구분하여 dfs
            if info[nxt] == 0:
                max_cnt = max(max_cnt, dfs(s + 1, w, new_candidates))
            else:
                max_cnt = max(max_cnt, dfs(s, w + 1, new_candidates))
        
        return max_cnt
    
    return dfs(1, 0, graph[0])
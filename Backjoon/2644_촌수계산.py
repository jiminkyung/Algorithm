# 그래프 이론
# 너비 우선 탐색 (BFS)
# 깊이 우선 탐색 (DFS)


# 문제: https://www.acmicpc.net/problem/2644

# BFS로 풀이
# 메모리: 32412KB / 시간: 36ms
from sys import stdin


input = stdin.readline

def main():
    N = int(input())
    p, target = map(int, input().split())

    # ⭐parent랑 child로 나눌 필요 없음.
    # 어차피 부모나 자식이나 모두 촌수로는 1 차이나기 때문.
    # 그냥 graph[x] = x의 부모와 자식들 형태로 저장해도 됨~
    parent = [0] * (N+1)
    child = [[] for _ in range(N+1)]

    M = int(input())

    for _ in range(M):
        x, y = map(int, input().split())
        parent[y] = x
        child[x].append(y)
    

    def bfs(p, target) -> int:
        visited = [False] * (N+1)
        visited[p] = True
        curr = [(p, 0)]  # (현재 사람, p와의 촌수)

        while curr:
            nxt = []
            for x, cnt in curr:
                if x == target:
                    return cnt
                
                # 부모가 있고 아직 확인하지 않았다면
                if parent[x] != 0 and not visited[parent[x]]:
                    nxt.append((parent[x], cnt+1))
                    visited[parent[x]] = True
                
                # 자식이 없는 사람이라면 pass
                if not child[x]:
                    continue
                # 있다면 아직 확인하지 않은 자식들만 검사
                for c in child[x]:
                    if not visited[c]:
                        nxt.append((c, cnt+1))
                        visited[c] = True
            
            curr = nxt
        return -1  # 관계 없는 사람이면 -1 반환
    

    print(bfs(p, target))


main()
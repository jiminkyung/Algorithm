# 그래프 이론
# 문자열
# 최소 스패닝 트리


# 문제: https://www.acmicpc.net/problem/1414

# 모든 간선정보가 주어지길래 프림으로 풀려 했으나...
# 예제 3 같은 케이스가 존재함. (2 -> 3, 4 -> 3 루트만 존재.)
# 🗝️프림 풀이 시 단방향 -> 양방향(무방향) 간선으로 먼저 처리해줘야 함. 크루스칼은 그냥 풀어도 됨.
# => graph[i][j]와 graph[j][i] 중 더 작은 값을 i-j 랜선 길이로 저장하고 프림 실행.

# 1) 프림 풀이
# 메모리: 32412KB / 시간: 40ms
from sys import stdin


input = stdin.readline
INF = int(1e9)

def main():
    N = int(input())
    # 알파벳과 숫자 맵핑. 0은 INF로 설정.
    alphabet = {alp: i for i, alp in enumerate("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", start=1)}
    alphabet["0"] = INF
    graph = [list(map(lambda x: alphabet[x], input().rstrip())) for _ in range(N)]
    ret = 0

    for i in range(N):
        for j in range(N):
            # i-j 간선이 0이 아닐경우 전체 랜선 길이값에 더해줌.
            # i-j, j-i 중 더 작은값을 i-j 사이의 간선 값으로 설정. (무방향)
            if graph[i][j] != INF:
                ret += graph[i][j]
            graph[i][j] = min(graph[i][j], graph[j][i])
    
    length = [INF] * N
    visited = [False] * N
    length[0] = 0

    for _ in range(N):
        min_length = INF
        min_node = -1

        for i in range(N):
            if not visited[i] and length[i] < min_length:
                min_length = length[i]
                min_node = i
        
        # 갈 수 있는 노드가 없다면 모든 컴퓨터 연결 불가!
        if min_node == -1:
            print(-1)
            return
        
        visited[min_node] = True
        ret -= min_length

        for nxt in range(N):
            if visited[nxt] or length[nxt] <= graph[min_node][nxt]:
                continue
            length[nxt] = graph[min_node][nxt]
    

    print(ret)


main()


# 2) 크루스칼 풀이
# 메모리: 32544KB / 시간: 40ms
from sys import stdin


input = stdin.readline
INF = int(1e9)

def main():
    N = int(input())
    alphabet = {alp: i for i, alp in enumerate("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", start=1)}
    alphabet["0"] = INF

    parent = list(range(N))
    graph = []

    # 어차피 정렬 후 연결 -> parent를 통해 MST에 포함되어있는지 판단하기 때문에, 무방향 처리 없이 바로 추가해줘도 됨.
    for i in range(N):
        line = list(map(lambda x: alphabet[x], input().rstrip()))
        for j in range(N):
            graph.append((i, j, line[j]))
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(a, b):
        a, b = find(a), find(b)

        if a != b:
            if parent[a] < parent[b]:
                parent[b] = a
            else:
                parent[a] = b
            return True
        
        return False
    

    ret = 0

    graph.sort(key=lambda x: x[2])
    
    # 0이 아닌 모든 랜선의 길이 저장
    ret = sum(w for _, _, w in graph if w != INF)

    for u, v, w in graph:
        # 0이면 pass
        if w == INF:
            continue
        if union(u, v):
            ret -= w
    
    # 모든 컴퓨터가 이어져있다면 결과값을, 아니라면 -1 출력
    p = parent[0]
    print(ret if all(find(i) == p for i in range(N)) else -1)


main()
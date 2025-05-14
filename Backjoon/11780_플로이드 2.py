# 동적 계획법과 최단거리 역추적


# 문제: https://www.acmicpc.net/problem/11780

# 🚨 시작도시-도착도시 가 같은 경우는 없다.
# => 중복 경로가 없다는 의미가 아니라, 1 1 2 처럼 u == v인 경우가 없다는 뜻이다.
# 즉, 입력값을 저장할 때 기존의 값보다 작은지 체크해야한다.

# 🐛 (25/05/14) 간선 정보 입력부분 수정.
# - 새로운 값 c가 graph[a][b]보다 작을때에만 nxt[a][b] = b로 갱신해야함.
# - 이전 풀이에서는 무조건 갱신하도록 작성했지만 통과함. 운이 좋았던모양?

# 1) 새로운 풀이
# 메모리: 33432KB / 시간: 212KB
from sys import stdin


input = stdin.readline
INF = int(1e9)

def main():
    n = int(input())
    m = int(input())

    graph = [[INF] * (n+1) for _ in range(n+1)]
    nxt = [[-1] * (n+1) for _ in range(n+1)]  # nxt[a][b] = a에서 b로 가기 위해 방문해야할 첫번째 노드

    # 1. 간선 정보 저장
    for i in range(1, n+1):
        graph[i][i] = 0
    
    for _ in range(m):
        a, b, c = map(int, input().split())
        # 새로운 비용 c가 기존 비용보다 작을때에만 graph, nxt 갱신
        if c < graph[a][b]:
            graph[a][b] = c
            nxt[a][b] = b  # nxt도 기존 비용보다 작을때에만 갱신!


    # 2. 플로이드-워셜 수행
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                cost = graph[i][k] + graph[k][j]
                # k를 거치는 비용이 기존 비용보다 작다면 갱신
                if cost < graph[i][j]:
                    graph[i][j] = cost
                    nxt[i][j] = nxt[i][k]  # i-k의 경로 값을 i-j에 저장
    

    def get_path(s: int, e: int) -> list:
        """
        경로 역추적 함수
        - [a, [b, [c, [d, [e]]]]] 이런식으로, 가장 바깥괄호부터 안쪽 괄호까지 파고든다고 생각하면 됨.
        - s가 a -> b -> c -> d -> e로 변화하게 되는것!
        - 진행 과정 예시
            - 초기 path = [a]
            - a에서 e로 가기 위해 가장 첫번째로 방문해야 할 노드 = b, path = [a, b]
            - b에서 e로 가기 위해 가장 첫번째로 방문해야 할 노드 = c, path = [a, b, c]
            - c에서 e로 가기 위해 가장 첫번째로 방문해야 할 노드 = d, path = [a, b, c, d]
            - d에서 e로 가기 위해 가장 첫번째로 방문해야 할 노드 = e, path = [a, b, c, d, e]
        """
        path = [s]
        while s != e:
            s = nxt[s][e]
            path.append(s)
        return path
    

    # 3. 최소비용 출력
    for i in range(1, n+1):
        print(" ".join(map(lambda x: str(x) if x != INF else "0", graph[i][1:])))
    
    # 4. 경로 추적 후 출력
    for i in range(1, n+1):
        for j in range(1, n+1):
            # 시작점 == 끝점 이거나, i-j로 가는 경로가 없다면 0 출력
            if i == j or graph[i][j] == INF:
                print(0)
            else:
                path = get_path(i, j)
                print(len(path), *path)


main()


# 2) 기존 풀이
# 메모리: 42140KB / 시간: 228ms
from sys import stdin


input = stdin.readline
INF = int(1e9)


def floyd_warshall(v, route: list) -> list:
    dp = [[INF] * v for _ in range(v)]
    nxt = [[-1] * v for _ in range(v)]  # nxt[i][j] = i에서 j로 가는 경로에서 i 다음에 방문해야 할 노드
    # 0으로 초기화 시, 0번 도시(실제로는 1번도시)인 경우와 혼동될 수 있으므로 -1로 초기화한다.

    for i in range(v):
        dp[i][i] = 0
    
    for a, b, c in route:
        if c < dp[a-1][b-1]:  # 기존 경로값보다 작으면 업데이트.
            dp[a-1][b-1] = c
        nxt[a-1][b-1] = b-1
    
    for k in range(v):
        for i in range(v):
            for j in range(v):
                if dp[i][k] + dp[k][j] < dp[i][j]:
                    dp[i][j] = dp[i][k] + dp[k][j]
                    nxt[i][j] = nxt[i][k]  # i 다음에 방문해야 할 노드 저장
    return dp, nxt


# 경로추적 함수
def get_path(nxt: list, s, e) -> list:
    if nxt[s][e] == -1:  # s에서 e로 갈 수 있는 경로가 없다면(-1) 빈 리스트 반환.
        return []
    
    path = [s]
    while s != e:
        s = nxt[s][e]
        path.append(s)
    return path


n = int(input())
m = int(input())
route = [tuple(map(int, input().split())) for _ in range(m)]

dp, nxt = floyd_warshall(n, route)

for i in range(n):
    # print(*[0 if d == INF else d for d in dp[i]])  # join을 사용하는 방식이 조금 더 빠르다.
    print(" ".join(map(lambda x: "0" if x == INF else str(x), dp[i])))

for i in range(n):
    for j in range(n):
        if i == j or dp[i][j] == INF:
            print(0)
        else:
            path = get_path(nxt, i, j)
            # print(len(path), *[p+1 for p in path])
            print(len(path), " ".join(map(lambda x: str(x+1), path)))
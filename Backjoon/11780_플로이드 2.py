# 동적 계획법과 최단거리 역추적


# 시작도시-도착도시 가 같은 경우는 없다 => 중복 경로가 없다는 의미가 아니라, 1 1 2 처럼 u == v인 경우가 없다는 뜻이다.
# 즉, 입력값을 저장할 때 기존의 값보다 작은지 체크해야한다.

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
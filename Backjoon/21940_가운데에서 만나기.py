# 문제집 - 0x1C강 - 플로이드 알고리즘


# 문제: https://www.acmicpc.net/problem/21940

# 1) 새롭게 작성한 풀이
# 메모리: 33432KB / 시간: 924ms
from sys import stdin


input = stdin.readline
INF = int(1e9)

def main():
    def floyd_warshall(graph: list) -> list:
        for k in range(N):
            for i in range(N):
                for j in range(N):
                    graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
        return graph


    def calc() -> list[int]:
        """ X가 될 수 있는 마을 후보들 구하기 """
        min_time = INF  # 최소 왕복시간
        towns = []  # X가 될 수 있는 마을들

        # 최대가 최소 = X까지 가는 왕복시간 중 최댓값이, 다른 마을로 가는 왕복시간들 중 최솟값인경우.
        for X in range(N):
            time = 0  # 현재 마을 기준 최대 왕복시간
            for curr in C:
                curr_time = graph[curr][X] + graph[X][curr]
                if curr_time == INF:
                    break
                time = max(time, curr_time)
            
            # 만약 다른 마을 왕복시간보다 작다면, 최솟값과 town 리스트 갱신.
            # 같다면 town 리스트에 현재 마을 추가
            if time < min_time:
                towns = [X]
                min_time = time
            elif time == min_time:
                towns.append(X)
        return towns
    

    N, M = map(int, input().split())
    graph = [[INF] * N for _ in range(N)]

    for i in range(N):
        graph[i][i] = 0
    
    for _ in range(M):
        A, B, T = map(int, input().split())
        graph[A-1][B-1] = T
    
    K = int(input())
    C = list(map(lambda x: int(x)-1, input().split()))
    
    graph = floyd_warshall(graph)
    towns = calc()
    
    print(" ".join(map(lambda x: str(x+1), towns)))


main()


# 2) 기존 풀이. 딕셔너리 사용.
# 메모리: 34456KB / 시간: 2632ms
from sys import stdin


input = stdin.readline
INF = float("inf")

N, M = map(int, input().split())
graph = [[INF] * (N+1) for _ in range(N+1)]

# 단방향으로 저장해줘야함.
for _ in range(M):
    A, B, T = map(int, input().split())
    graph[A][B] = T

K = map(int, input().split())
position = list(map(int, input().split()))

for i in range(1, N+1):
    graph[i][i] = 0

# 플로이드-워셜 수행
for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            graph[i][j] = min(graph[i][k] + graph[k][j], graph[i][j])

# 거리가 동일한 친구들을 리스트에 저장해둠
distance = {}

for town in range(1, N+1):
    dis = 0
    # 친구들과 town과의 거리값을 구함.
    # 거리값들 중 가장 큰 값을 dis로 기록해둠.
    for pos in position:
        curr_dis = graph[pos][town] + graph[town][pos]
        dis = max(curr_dis, dis)
    
    if distance.get(dis, 0) == 0:
        distance[dis] = [town]
    else:
        distance[dis].append(town)

# 최대 거리값들 중 가장 최소값을 찾고, 해당되는 town들을 출력.
min_dis = min(distance)
print(*distance[min_dis])


# ❓ 같은 로직임에도 불구하고 실행시간이 600대인 풀이들이 많음. 이유가 뭔지?
# => 함수로 분리 / float대신 int사용 / 딕셔너리 대신 리스트로 바로 최소값 갱신 ...etc

# 리스트로 최소값을 바로 갱신하는 버전
# 실행시간: 2656ms
from sys import stdin


input = stdin.readline
INF = float("inf")

N, M = map(int, input().split())
graph = [[INF] * (N+1) for _ in range(N+1)]

for _ in range(M):
    A, B, T = map(int, input().split())
    graph[A][B] = T

K = map(int, input().split())
position = list(map(int, input().split()))

for i in range(1, N+1):
    graph[i][i] = 0


for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            graph[i][j] = min(graph[i][k] + graph[k][j], graph[i][j])

ret = []
min_dis = INF

for town in range(1, N+1):
    dis = max(graph[pos][town] + graph[town][pos] for pos in position)
    if dis < min_dis:
        ret = [town]
        min_dis = dis
    elif dis == min_dis:
        ret.append(town)


print(*ret)
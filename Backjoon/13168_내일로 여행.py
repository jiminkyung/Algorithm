# 문제집 - 0x1C강 - 플로이드 알고리즘


# 문제: https://www.acmicpc.net/problem/13168
# 메모리: 33432KB / 시간: 720ms
from sys import stdin


input = stdin.readline
INF = int(1e9)

N, R = map(int, input().split())
R *= 2
data = set(input().rstrip().split())
cities = {d: i for i, d in enumerate(data)}

M = int(input())
trip_cities = [cities[city] for city in input().rstrip().split()]

# 🚨 그냥 정수 나눗셈 // 처리를 해주면 틀림...
# 해결방법 1. 실수형으로 계산, 2. 2배 해준뒤 // 사용
def calc(city, cost):
    if city in ("Mugunghwa", "ITX-Saemaeul", "ITX-Cheongchun"):
        return 0
    if city in ("S-Train", "V-Train"):
        return cost // 2
    return cost


ticket = [[INF] * N for _ in range(N)]
normal = [[INF] * N for _ in range(N)]
K = int(input())

for _ in range(K):
    T, S, E, cost = input().rstrip().split()

    S, E = cities[S], cities[E]
    cost = int(cost) * 2

    ticket_cost = calc(T, cost)
    ticket[S][E] = min(ticket_cost, ticket[S][E])
    ticket[E][S] = min(ticket_cost, ticket[E][S])

    normal[S][E] = min(cost, normal[S][E])
    normal[E][S] = min(cost, normal[E][S])

for k in range(N):
    for i in range(N):
        for j in range(N):
            ticket[i][j] = min(ticket[i][k] + ticket[k][j], ticket[i][j])
            normal[i][j] = min(normal[i][k] + normal[k][j], normal[i][j])

# 티켓을 사지 않았을경우의 비용
normal_cost = sum(normal[trip_cities[i]][trip_cities[i+1]] for i in range(M-1))


# 중간에 티켓을 구매할 경우를 고려해서 계산해야함.
def total_cost(start, cost):
    for i in range(start, M-1):
        cost += ticket[trip_cities[i]][trip_cities[i+1]]
    
    return cost

min_cost = INF

curr_cost = 0
for start in range(M-1):
    cost = total_cost(start, curr_cost) + R
    min_cost = min(cost, min_cost)
    curr_cost += normal[trip_cities[start]][trip_cities[start+1]]

print("Yes" if min_cost < normal_cost else "No")
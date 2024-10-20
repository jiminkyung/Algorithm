# 문제집 - BOJ 길라잡이 베타 (1)


# 문제: https://www.acmicpc.net/problem/15686

# 참고👉 https://velog.io/@mechauk418/%EB%B0%B1%EC%A4%80-15686%EB%B2%88-%EC%B9%98%ED%82%A8-%EB%B0%B0%EB%8B%AC-%ED%8C%8C%EC%9D%B4%EC%8D%AC%EB%B0%B1%ED%8A%B8%EB%9E%98%ED%82%B9
# 메모리: 31120KB / 시간: 364ms
from sys import stdin


input = stdin.readline

def dfs(idx, cnt):
    global min_dis

    if cnt == M:
        ans = 0
        for h in house:
            dis = int(1e9)
            for i in range(len(chick)):
                if visited[i]:
                    curr_dis = abs(h[0] - chick[i][0]) + abs(h[1] - chick[i][1])
                    dis = min(dis, curr_dis)
            ans += dis
            if ans >= min_dis:
                return
        min_dis = min(min_dis, ans)
        return
    
    for i in range(idx, len(chick)):
        if not visited[i]:
            visited[i] = True
            dfs(i, cnt+1)
            visited[i] = False


N, M = map(int, input().split())
road = [list(map(int, input().split())) for _ in range(N)]

house = []
chick = []

for i in range(N):
    for j in range(N):
        if road[i][j] == 1:
            house.append((i, j))
        elif road[i][j] == 2:
            chick.append((i, j))

visited = [False] * len(chick)
min_dis = int(1e9)

dfs(0, 0)
print(min_dis)
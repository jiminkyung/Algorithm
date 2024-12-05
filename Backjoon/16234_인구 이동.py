# 문제집 - 0x0D강 - 시뮬레이션


# 문제: https://www.acmicpc.net/problem/16234
# 메모리: 31120KB / 시간: 2388ms
from sys import stdin


input = stdin.readline

N, L, R = map(int, input().split())

nations = [list(map(int, input().split())) for _ in range(N)]
day = 0

def bfs(x, y):
    curr = [(x, y)]
    visited[x][y] = True
    open = {(x, y)}

    while curr:
        nxt = []
        for x, y in curr:
            for nx, ny in ((x-1, y), (x+1, y), (x, y-1), (x, y+1)):
                if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                    if L <= abs(nations[x][y] - nations[nx][ny]) <= R:
                        nxt.append((nx, ny))
                        open.add((nx, ny))
                        visited[nx][ny] = True
        curr = nxt
    if len(open) > 1:
        unions.append(list(open))


while True:
    unions = []
    visited = [[False] * N for _ in range(N)]

    for i in range(N):
        # for j in range(N):
        # 아래의 홀수/짝수 좌표만 솎아내는 방식을 적용하니 실행시간이 반절 가량 줄었다!
        # 적용 전: 4132ms, 적용 후: 2388ms
        for j in range(i%2, N, 2):
            if not visited[i][j]:
                bfs(i, j)
    
    if not unions:
        break

    for union in unions:
        people = sum(nations[x][y] for x, y in union) // len(union)
        for x, y in union:
            nations[x][y] = people
    
    day += 1

print(day)


# 실행시간이 빠른 케이스들을 찾아보니 풀이방식이 모두 같았다.
# 메모리: 32140KB / 시간: 136ms
from sys import stdin
input = stdin.readline

def integrate(row, col, visited, date):
    global L, R, population, neigh

    queue = [(row, col)]
    pivot = 0
    q_len = 1
    pop_tot = population[row][col]
    visited[row][col] = date
    while pivot < q_len:
        r, c = queue[pivot]
        for nr, nc in neigh[(r,c)]:
            if (visited[nr][nc] < date) and (L <= abs(population[r][c] - population[nr][nc]) <= R):
                visited[nr][nc] = date
                queue.append((nr, nc))
                pop_tot += population[nr][nc]
                q_len += 1
        pivot += 1
    return queue, q_len, pop_tot

def solve():
    global population

    # 홀수/짝수 번갈아가며 좌표 저장
    queue = [(r, c) for c in range(N) for r in range(c%2, N, 2)]
    visited = [[-1] * N for _ in range(N)]
    for day in range(2000):
        next_q = []
        for r, c in queue:
            if visited[r][c] < day:
                q, q_len, pop_tot = integrate(r, c, visited, day)
                if q_len > 1:
                    avg = pop_tot//q_len
                    next_q += q
                    for x, y in q:
                        population[x][y] = avg

        if not next_q:
            print(day)
            break
        else:
            queue = next_q


if __name__ == "__main__":
    N, L, R = map(int, input().split())
    population = [list(map(int, input().split())) for _ in range(N)]
    neigh = {}
    for r in range(N):
        for c in range(N):
            tmp = []
            for nr, nc in [(r,c-1), (r,c+1), (r-1,c), (r+1,c)]:
                if (0 <= nr < N) and (0 <= nc < N):
                    tmp.append((nr, nc))
            neigh[(r,c)] = tmp
    solve()
# 동적 계획법과 최단거리 역추적

# 어려웠던 문제다... 나중에 꼭 다시 스스로 풀어봐야할 문제.


# 참고👉 https://velog.io/@j2noo/%EB%B0%B1%EC%A4%80BOJ-2618-%EA%B2%BD%EC%B0%B0%EC%B0%A8-%EC%A0%91%EA%B7%BC%EA%B3%BC-%ED%92%80%EC%9D%B4Python
# 메모리: 78072KB / 시간: 3096ms
import sys


sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def cal(m, n):
    ret = abs(cases[m][0] - cases[n][0]) + abs(cases[m][1] - cases[n][1])
    return ret


def dfs(m, n):
    nxt = max(m, n) + 1

    if nxt == W+2:
        return 0
    
    if dp[m][n]:
        return dp[m][n]
    
    case1 = dfs(nxt, n) + cal(m, nxt)
    case2 = dfs(m, nxt) + cal(n, nxt)

    if case1 < case2:
        path[m][n] = 1
        dp[m][n] = case1
    else:
        path[m][n] = 2
        dp[m][n] = case2
    
    return dp[m][n]


N = int(input())
W = int(input())
cases = [(1, 1), (N, N)] + [tuple(map(int, input().split())) for _ in range(W)]

dp = [[0] * (W+2) for _ in range(W+2)]
path = [[0] * (W+2) for _ in range(W+2)]

print(dfs(0, 1))  # 두 경찰차의 초기 위치

m, n = 0, 1
for i in range(2, W+2):
    print(path[m][n])
    if path[m][n] == 1:
        m = i
    else:
        n = i


# 또다른 풀이 방법. 재귀 깊이를 늘려주지 않아도 된다.
# 참고👉 https://blog.everdu.com/423
# 메모리: 182124KB / 시간: 1904ms => 첫번째 코드와 비교해 시간이 절반인대신 메모리는 두배가량 차이난다.
def calc_dist(pos1, pos2):
    return abs(pos1[0]-pos2[0]) + abs(pos1[1]-pos2[1])

INF = 9876543210
n = int(input())
w = int(input())
accidents = [(-1, -1)] + [tuple(map(int, input().split())) for _ in range(w)]
dp = [[-1 for _ in range(w+1)] for _ in range(w+1)]
dp[0][0] = 0
dp[1][0] = calc_dist((1, 1), accidents[1])
dp[0][1] = calc_dist((n, n), accidents[1])

prev_pos = [[None for _ in range(w+1)] for _ in range(w+1)]

for j in range(w+1):
    for i in range(w+1):
        if i == j or dp[i][j] != -1:
            continue
        if i > j:
            if i - j == 1:
                min_value = INF
                min_pos = None
                for k in range(i-1):
                    if k == 0:
                        accidents[k] = (1, 1)
                    if dp[k][j] + calc_dist(accidents[k], accidents[i]) < min_value:
                        min_value = dp[k][j] + calc_dist(accidents[k], accidents[i])
                        min_pos = (k, j)

                dp[i][j] = min_value
                prev_pos[i][j] = min_pos
            elif i - j > 1:
                dp[i][j] = dp[i-1][j] + calc_dist(accidents[i], accidents[i-1])
                prev_pos[i][j] = (i-1, j)

        else: # j > i
            if j - i == 1:
                min_value = INF
                min_pos = None
                for k in range(j-1):
                    if k == 0:
                        accidents[k] = (n, n)
                    if dp[i][k] + calc_dist(accidents[k], accidents[j]) < min_value:
                        min_value = dp[i][k] + calc_dist(accidents[k], accidents[j])
                        min_pos = (i, k)
                dp[i][j] = min_value
                prev_pos[i][j] = min_pos
            elif j - i > 1:
                dp[i][j] = dp[i][j-1] + calc_dist(accidents[j], accidents[j-1])
                prev_pos[i][j] = (i, j-1)

answer = INF
pos = (-1, -1)
for i in range(w):
    if dp[i][w] < answer:
        answer = dp[i][w]
        pos = (i, w)
for j in range(w):
    if dp[w][j] < answer:
        answer = dp[w][j]
        pos = (w, j)

print(answer)
path = []
while w > 0:
    if pos[0] == w:
        path.append(1)
    else:
        path.append(2)

    w -= 1
    pos = prev_pos[pos[0]][pos[1]]
    
for car in reversed(path):
    print(car)
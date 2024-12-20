# 문제집 - 0x0D강 - 시뮬레이션


# 문제: https://www.acmicpc.net/problem/17406

# 15683_감시, 17144_미세먼지 안녕! 문제와 비슷하다.
# 메모리: 32412KB / 시간: 192ms
from sys import stdin


input = stdin.readline

N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
rotation = []
for _ in range(K):
    r, c, s = map(int, input().split())
    rotation.append((r-1, c-1, s))
min_value = int(1e9)


# 회전 입력값대로 배열을 회전시키는 함수
def rotate(arr_copy, rot):
    r, c, s = rot

    for k in range(s, 0, -1):
        # 꼭지점 저장해두기
        vertex = arr_copy[r+k][c+k]

        # 위 -> 아래 (오른쪽 변)
        for i in range(r+k, r-k, -1):
            arr_copy[i][c+k] = arr_copy[i-1][c+k]
        
        # 왼쪽 -> 오른쪽 (윗쪽 변)
        for j in range(c+k, c-k, -1):
            arr_copy[r-k][j] = arr_copy[r-k][j-1]
        
        # 아래 -> 위 (왼쪽 변)
        for i in range(r-k, r+k):
            arr_copy[i][c-k] = arr_copy[i+1][c-k]
        
        # 오른쪽 -> 왼쪽 (아랫쪽 변)
        for j in range(c-k, c+k):
            arr_copy[r+k][j] = arr_copy[r+k][j+1]
        arr_copy[r+k][c+k-1] = vertex


# 배열의 값을 구하는 함수
def counting(arr_copy):
    value = min(sum(line) for line in arr_copy)
    return value


used = [False] * K
# 백트래킹 함수
def dfs(depth, arr):
    global min_value
    if depth == K:
        min_value = min(counting(arr), min_value)
        return
    
    for i in range(K):
        if used[i]:
            continue
        # 매 턴마다 인자로 받은 arr을 카피함. 카피한 arr은 rotate, dfs 실행 시 던져준다.
        # 기존의 arr은 다음 턴에서 무리 없이 사용된다.
        arr_copy = [line[:] for line in arr]
        used[i] = True
        rotate(arr_copy, rotation[i])
        dfs(depth+1, arr_copy)
        used[i] = False

dfs(0, arr)
print(min_value)
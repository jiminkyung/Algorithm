# 누적 합

# 시간초과. 역시 너무 쉽다했더니...
from sys import stdin


input = stdin.readline

N, K = map(int, input().split())
arr = list(map(int, input().split()))

for _ in range(K):
    i, j = map(int, input().split())
    print(sum(arr[i-1:j]))


# 2차시도
# 메모리 초과~!
from sys import stdin


input = stdin.readline

N, K = map(int, input().split())
arr = list(map(int, input().split()))

def dynamic(start: int, end: int) -> int:
    dp = [[0]*(N+1) for _ in range(N+1)]

    for i in range(1, N+1):
        for j in range(i, N+1):
            dp[i][j] = dp[i][j-1] + arr[j-1]
    
    return dp[start][end]

for _ in range(K):
    start, end = map(int, input().split())
    print(dynamic(start, end))


# 딕셔너리를 사용해보자 => 이것도 메모리 초과!
from sys import stdin


input = stdin.readline

N, K = map(int, input().split())
arr = tuple(map(int, input().split()))

def dynamic(start: int, end: int) -> int:
    dp = {}

    for i in range(1, N+1):
        for j in range(i, N+1):
            dp[(i, j)] = dp.get((i, j-1), 0) + arr[j-1]
    
    return dp[(start, end)]

for _ in range(K):
    start, end = map(int, input().split())
    print(dynamic(start, end))


# 그냥 구간합을 구해놓고 계산하면 되는 문제였다. dp는 잊어버리자...
# 메모리: 41276KB / 시간: 268ms
from sys import stdin


input = stdin.readline
N, K = map(int, input().split())
arr = list(map(int, input().split()))

sum_arr = [0]
curr = 0

for a in arr:
    curr += a
    sum_arr.append(curr)

for _ in range(K):
    i, j = map(int, input().split())
    print(sum_arr[j] - sum_arr[i-1])


# 메모리 48464, 시간 136ms인 코드!
    # accumulate: 누적 결과를 반환하는 iterator.
    # splitlines: 줄바꿈을 기준으로 문자열을 리스트로 변환.
from itertools import*
from sys import*
if __name__ == "__main__":
    Q=map(str.split, stdin.read().splitlines())
    next(Q)
    A = list(accumulate(map(int, next(Q)),initial=0))
    stdout.write('\n'.join(f'{A[int(b)]-A[int(a)-1]}'for a,b in Q))
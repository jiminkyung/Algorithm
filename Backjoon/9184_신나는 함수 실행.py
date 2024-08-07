# 동적 계획법 1
# AI선생님과 함께한 풀이

# 메모리: 31120KB / 시간: 72ms

from sys import stdin


input = stdin.readline

def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)

    if dp[a][b][c] != 0:
        return dp[a][b][c]

    if a < b < c:
        dp[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
    else:
        dp[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
    
    return dp[a][b][c]

dp = [[[0 for _ in range(21)] for _ in range(21)] for _ in range(21)]

while True:
    a, b, c = map(int, input().split())

    if a == -1 and b == -1 and c == -1:
        break

    print(f"w({a}, {b}, {c}) = {w(a, b, c)}")


# 바이트 문자열로 실행시간 줄여보기 => 68ms
import sys


input = sys.stdin.buffer.readline
write = sys.stdout.buffer.write

def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)

    if dp[a][b][c] != 0:
        return dp[a][b][c]

    if a < b < c:
        dp[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
    else:
        dp[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
    
    return dp[a][b][c]

dp = [[[0 for _ in range(21)] for _ in range(21)] for _ in range(21)]

while True:
    a, b, c = map(int, input().split())

    if a == -1 and b == -1 and c == -1:
        break

    write(b"w(%d, %d, %d) = %d\n" % (a, b, c, w(a, b, c)))
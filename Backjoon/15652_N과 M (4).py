# 백트래킹
# 메모리: 31120KB / 시간: 48ms

import sys


def backtrack(n, m, start, ret):
    if len(ret) == m:
        sys.stdout.buffer.write(b" ".join(ret) + b"\n")
        return
    
    for i in range(start, n+1):
        ret.append(str(i).encode())
        backtrack(n, m, i, ret)
        ret.pop()

N, M = map(int, sys.stdin.buffer.readline().split())
backtrack(N, M, 1, [])
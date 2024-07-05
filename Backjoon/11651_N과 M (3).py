# 백트래킹
# 메모리: 31120KB / 시간: 1936ms

def backtrack(n, m, ret):
    if len(ret) == m:
        print(*ret)
        return
    
    for i in range(1, n+1):
        ret.append(i)
        backtrack(n, m, ret)
        ret.pop()

N, M = map(int, open(0).read().split())
backtrack(N, M, [])


# sys모듈, 바이트 문자열을 사용하여 실행시간 단축하기
# 메모리: 31120KB / 시간: 548ms
import sys


def backtrack(n, m, ret):
    if len(ret) == m:
        sys.stdout.buffer.write(b" ".join(ret) + b"\n")
        return
    
    for i in range(1, n+1):
        ret.append(str(i).encode())
        backtrack(n, m, ret)
        ret.pop()

N, M = map(int, sys.stdin.buffer.readline().split())
backtrack(N, M, [])
sys.stdout.buffer.flush()
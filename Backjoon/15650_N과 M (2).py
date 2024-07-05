# 백트래킹
# 메모리: 31120KB / 시간: 40ms

def backtrack(n, m, start, ret):
    if len(ret) == m:
        print(*ret)
        return
    
    for i in range(start, n+1):
        ret.append(i)
        backtrack(n, m, i+1, ret)
        ret.pop()

N, M = map(int, open(0).read().split())
backtrack(N, M, 1, [])
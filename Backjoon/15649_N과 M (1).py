# 백트래킹
# 메모리: 31120KB / 시간: 204ms

N, M = map(int, open(0).read().split())

def backtrack(n, m, size, ret):
    if size == m:
        print(*ret)
        return
    
    for i in range(1, n+1):
        if i not in ret:
            ret.append(i)
            backtrack(n, m, size+1, ret)
            ret.pop()

backtrack(N, M, 0, [])
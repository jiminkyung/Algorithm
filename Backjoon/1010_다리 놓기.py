# 조합론
# 메모리: 31120KB / 시간: 36ms

# "다리끼리는 겹쳐질 수 없다" 때문에 복잡해보이지만 nCk와 같다.

from sys import stdin


input = stdin.readline

def bridge(n, k):
    ret = 1

    for i in range(k):
        ret *= (n-i)
    
    for i in range(1, k+1):
        ret //= i
    
    return ret

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    print(bridge(M, N))
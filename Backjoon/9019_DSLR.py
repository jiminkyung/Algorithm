# 동적 계획법과 최단거리 역추적


# 첫번째 시도. 시간초과. 불필요한 부분이 많음.
from sys import stdin
from collections import deque


input = stdin.readline
MOD = 10000


def calc(n, order):
    ret = 0
    ret_order = ""

    if order == 0:
        ret = 2 * n % MOD
        ret_order = "D"
    elif order == 1:
        if n > 0:
            ret = n - 1
        else:
            ret = 9999
        ret_order = "S"
    elif order == 2:
        n = str(n)
        ret = int(n[1:] + n[0])
        ret_order = "L"
    else:
        n = str(n)
        ret = int(n[-1] + n[:-1])
        ret_order = "R"
    
    return ret, ret_order


def bfs(start, end) -> list:
    queue = deque([start])
    visited = [False] * 10001
    path = [0] * 10001

    while queue:
        curr = queue.popleft()

        if curr == end:
            return path
        
        for i in range(4):
            n, order = calc(curr, i)

            if 0 <= n <= 10000 and not visited[n]:
                queue.append(n)
                visited[n] = True
                path[n] = (curr, order)

T = int(input())

for _ in range(T):
    s, e = map(int, input().split())
    path = bfs(s, e)
    ret = ""
    tmp = e

    while tmp != s:
        nxt, order = path[tmp]
        ret += order
        tmp = nxt
    
    print(ret[::-1])


# 두번째 시도. 따로 path 리스트를 생성하지 않고 문자열에 방향값 저장해주기.
# 실패... 인데, 대부분 pypy3로 제출한 듯 하다.
# Pypy3로 제출, 메모리: 214032KB / 시간: 8328ms
from sys import stdin
from collections import deque


input = stdin.readline

def calc(n, dis):
    if dis == "D":
        return 2 * n % 10000
    elif dis == "S":
        return n - 1 if n != 0 else 9999
    elif dis == "L":
        return (n % 1000) * 10 + n // 1000
    else:
        return (n % 10) * 1000 + n // 10

def bfs(start, end):
    queue = deque([(start, "")])
    visited = [False] * 10001
    visited[start] = True

    while queue:
        curr, path = queue.popleft()

        if curr == end:
            return path
        
        for dis in "DSLR":
            nxt = calc(curr, dis)
            if not visited[nxt]:
                visited[nxt] = True
                queue.append((nxt, path + dis))

T = int(input())

for _ in range(T):
    s, e = map(int, input().split())
    print(bfs(s, e))

# 🚨 질문게시글에서 발견한 조언 https://www.acmicpc.net/board/view/148921
"""
시간초과의 원인

1. visited같은 list자료구조의 조건문에서 not in/in 은 O(N)입니다.
2. 파이썬 문자열은 + 연산 시 새로운 문자열을 계속해서 만들어내기 때문에 시간/메모리적 효율이 매우 좋지 않습니다.
3. 그럼 지나왔던 방법은 어떻게 추적하는지?
지나왔던 경로에서 이전 경로를 저장하는 track 배열 하나를 만들고 track[next] = prev형식으로 저장해놓은 다음 도착지 > 출발지로 역 추적하는 방법이 있습니다.
"""


# Python3로 제출한 사람 중 1위인분의 코드. 양방향 BFS를 사용했다고 한다.
# 좀 더 공부해봐야겠다...
import sys



def sol(start, end):
    dp = [0] * L

    def bfs():
        dp[start] = 1
        dp[end] = -1
        queue_for = [start]
        queue_rev = [end]

        for i, j in zip(range(2, 5000), range(-2, -5000, -1)):
            queue2_for = []
            for q in queue_for:
                for k in path_for[q]:
                    if not dp[k]:
                        dp[k] = i
                        queue2_for.append(k)
                    
                    elif dp[k] < 0: return i-1, j+2, k               
            
            queue_for = queue2_for

            queue2_rev = []
            for q in queue_rev:
                for k in path_rev[q]:
                    if not dp[k]:
                        dp[k] = j
                        queue2_rev.append(k)

                    elif dp[k] > 0: return i-1, j+1, k       
            
            queue_rev = queue2_rev

    i, j, k = bfs()
    # 최단 경로 역추적
    answer = [None] * (i-j)

    a = k
    for b in range(i, 0, -1):
        for char, c in zip(('S', 'L', 'R', 'D', 'D'), path_rev[a]):
            if dp[c] == b:
                answer[b-1] = char
                a = c
                break
    
    a = k
    for b in range(j, 0):
        for char, c in zip(('S', 'L', 'R', 'D'), path_for[a]):
            if dp[c] == b:
                answer[b] = char
                a = c
                break
    
    return ''.join(answer)


readline = sys.stdin.readline
T = int(readline())
L = 10000
path_for = [(i-1 if i else 9999, 10*i%L + i//1000, i//10 + 1000*i%L, 2*i%L) for i in range(L)]
path_rev = [(0 if i == 9999 else i+1, i//10 + 1000*i%L, 10*i%L + i//1000, j := i//2, j+5000)
            if i % 2 == 0 else 
            (0 if i == 9999 else i+1, i//10 + 1000*i%L, 10*i%L + i//1000) for i in range(L)]

for _ in range(T):
    A, B = map(int, readline().split())

    sys.stdout.write(sol(A, B) + '\n')
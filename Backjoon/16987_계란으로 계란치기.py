# 문제집 - 0x0C강 - 백트래킹


# 문제: https://www.acmicpc.net/problem/16987

# 내구도, 무게를 한꺼번에 저장했을때
# 메모리: 31120KB / 시간: 3168ms
from sys import stdin


input = stdin.readline

N = int(input())
weight = []
hard = []

for _ in range(N):
    h, w = map(int, input().split())
    hard.append(h)
    weight.append(w)

ret = 0

def breaking(hard, weight, curr, total_broken):
    global ret

    if curr == N:
        ret = max(ret, total_broken)
        return
    
    if hard[curr] <= 0:
        breaking(hard, weight, curr+1, total_broken)
        return
    
    no_break = True

    for target in range(N):
        if target != curr and hard[target] > 0:
            no_break = False

            hard[target] -= weight[curr]
            hard[curr] -= weight[target]

            broken = total_broken
            if hard[curr] <= 0:
                broken += 1
            if hard[target] <= 0:
                broken += 1
            
            breaking(hard, weight, curr+1, broken)

            hard[target] += weight[curr]
            hard[curr] += weight[target]

    if no_break:
        breaking(hard, weight, curr+1, total_broken)

breaking(hard, weight, 0, 0)
print(ret)


# 내구도, 무게를 따로 저장했을때
# 메모리: 31120KB / 시간: 2780ms
from sys import stdin


input = stdin.readline

N = int(input())
weight = []
hard = []

for _ in range(N):
    h, w = map(int, input().split())
    hard.append(h)
    weight.append(w)

ret = 0

def breaking(hard, weight, curr, total_broken):
    global ret

    if curr == N:
        ret = max(ret, total_broken)
        return
    
    if hard[curr] <= 0:
        breaking(hard, weight, curr+1, total_broken)
        return
    
    no_break = True

    for target in range(N):
        if target != curr and hard[target] > 0:
            no_break = False

            hard[target] -= weight[curr]
            hard[curr] -= weight[target]

            broken = total_broken
            if hard[curr] <= 0:
                broken += 1
            if hard[target] <= 0:
                broken += 1
            
            breaking(hard, weight, curr+1, broken)

            hard[target] += weight[curr]
            hard[curr] += weight[target]

    if no_break:
        breaking(hard, weight, curr+1, total_broken)

breaking(hard, weight, 0, 0)
print(ret)
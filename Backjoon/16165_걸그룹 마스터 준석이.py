# 문제집 - 0x15강 - 해시


# 문제: https://www.acmicpc.net/problem/16165
# 메모리: 32412KB / 시간: 32ms
from sys import stdin


input = stdin.readline

N, M = map(int, input().split())
group = {}

for _ in range(N):
    name = input().rstrip()
    cnt = int(input())
    curr_group = [input().rstrip() for _ in range(cnt)]
    
    group[name] = curr_group

for _ in range(M):
    name = input().rstrip()
    flag = int(input())
    
    if flag:  # 1이면 그룹명 출력
        for k, v in group.items():
            if name in v:
                print(k)
    else:     # 0이면 그룹 인원 출력
        group[name].sort()
        print(*group[name], sep="\n")
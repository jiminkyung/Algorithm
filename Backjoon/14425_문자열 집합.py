# 집합과 맵
# 메모리: 36140KB / 시간: 3912ms

from sys import stdin


input = stdin.readline

N, M = map(int, input().split())

S = [input() for _ in range(N)]
ret = 0

for _ in range(M):
    string = input()
    if string in S:
        ret += 1

print(ret)


# 시간 64ms 코드...
import os
n,_,*s=os.read(0,os.fstat(0).st_size).split()
print(sum(map(set(s[:int(n)]).__contains__,s[int(n):])))
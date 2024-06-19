# 집합과 맵
# 메모리: 43924KB / 시간: 72ms

from sys import stdin


input = stdin.readline

N, M = map(int, input().split())

not_seen = {input().strip() for _ in range(N)}
not_heard = {input().strip() for _ in range(M)}

ret = sorted(not_seen & not_heard)
print(len(ret), *ret, sep="\n")
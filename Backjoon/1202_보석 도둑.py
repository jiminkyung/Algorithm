# 문제집 - BOJ 길라잡이 베타 (1)


# 문제: https://www.acmicpc.net/problem/1202
# 메모리: 86496KB / 시간: 1748ms
from sys import stdin
from heapq import heappop, heappush


input = stdin.readline

N, K = map(int, input().split())

jewl = []
for _ in range(N):
    heappush(jewl, tuple(map(int, input().split())))

sack = []
for _ in range(K):
    heappush(sack, int(input()))

taken_out = []
ret = 0
for _ in range(K):
    s = heappop(sack)

    # (현재 가방 s >= 가장 가벼운 보석의 무게) 라면, taken_out에 -(보석의 가치)를 넣는다.
    while jewl and s >= jewl[0][0]:
        _, v = heappop(jewl)
        heappush(taken_out, -v)
    # taken_out에 보석이 존재한다면 제일 가치가 높은 보석을 빼서 ret에 추가한다.
    if taken_out:
        ret -= heappop(taken_out)

print(ret)

# 가장 작은 가방부터 큰 가방 순으로 순회하기 때문에, 현재 턴의 s는 taken_out에 존재하는 보석을 100% 넣을 수 있다.
# 딕셔너리를 사용하는 풀이도 있지만 메모리가 너무 커지게된다.
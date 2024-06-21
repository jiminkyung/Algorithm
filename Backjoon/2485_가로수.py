# 약수, 배수와 소수 2단계
# 메모리: 38828KB / 시간: 164ms

"""
trees: 나무들의 위치
gaps: 각 나무 사이의 간격
n: 간격들의 최대공약수
ret: 새로 심어야 할 나무의 수
- 각 턴마다 끝점(이미 존재하는 가로수)값을 빼줘야한다. 즉 '간격//최대공약수 -1'
"""
from sys import stdin


input = stdin.readline

def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

N = int(input())

trees = sorted(int(input()) for _ in range(N))

gaps = []
for i in range(1, N):
    gaps.append(trees[i] - trees[i-1])

n = gaps[0]
for j in range(1, len(gaps)):
    n = gcd(n, gaps[j])

ret = 0
for gap in gaps:
    ret += gap//n - 1

print(ret)
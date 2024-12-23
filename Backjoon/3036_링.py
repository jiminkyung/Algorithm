# 문제집 - 0x12강 - 수학


# 문제: https://www.acmicpc.net/problem/3036
# 메모리: 32412KB / 시간: 36ms
from sys import stdin


input = stdin.readline

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


N = int(input())
rings = list(map(int, input().split()))
first_ring = rings[0]

for ring in rings[1:]:
    g = gcd(first_ring, ring)
    print(f"{first_ring // g}/{ring // g}")
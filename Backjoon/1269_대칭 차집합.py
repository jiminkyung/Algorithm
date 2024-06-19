# 집합과 맵
# 메모리: 110500KB / 시간: 296ms

from sys import stdin


input = stdin.readline

_ = input()
A, B = set(map(int, input().split())), set(map(int, input().split()))

print(len((A-B) | (B-A)))


# 신기한 숏코딩! str.split 은 처음봤다.
_,a,b=map(str.split,open(0))
print(len({*a}^{*b}))
# 심화 2
# 메모리: 31252KB / 시간: 36ms

from sys import stdin


input = stdin.readline

chong = set()
chong.add("ChongChong")
N = int(input())

for _ in range(N):
    h1, h2 = input().split()

    if h1 in chong:
        chong.add(h2)
    elif h2 in chong:
        chong.add(h1)

print(len(chong))


# set()을 좀 더 간략화하기. => update()사용!
# 보기엔 깔끔하지만 더 오래걸림. 시간: 40ms. 입력 크기가 클수록 효율적인가?
from sys import stdin


input = stdin.readline

chong = set(["ChongChong"])
N = int(input())

for _ in range(N):
    h1, h2 = input().split()
    
    if h1 in chong or h2 in chong:
        chong.update([h1, h2])

print(len(chong))
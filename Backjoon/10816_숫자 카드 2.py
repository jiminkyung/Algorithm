# 집합과 맵
# 메모리: 145736KB / 시간: 656ms


# 통과는 했으나 더 짧고 깔끔하게 풀 수 있을것같아서 아쉽다.

from sys import stdin


input = stdin.readline

N = int(input())
cards = map(int, input().split())
dic_cards = {}

for c in cards:
    dic_cards[c] = dic_cards.get(c, 0) + 1

M = int(input())
numbers = map(int, input().split())
print(" ".join(str(dic_cards.get(num, 0)) for num in numbers))


# 숏코딩 최강자 ㅋㅋ
from collections import*
_,a,_,b=open(0)
c=Counter(a.split())
for v in b.split():print(c[v])
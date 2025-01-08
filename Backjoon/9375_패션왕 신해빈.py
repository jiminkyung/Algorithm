# 문제집 - 0x15강 - 해시


# 문제: https://www.acmicpc.net/problem/9375
# 메모리: 32412KB / 시간: 32ms
from sys import stdin


input = stdin.readline

for _ in range(int(input())):
    N = int(input())

    clothes = {}
    for _ in range(N):
        _, value = input().rstrip().split()
        clothes[value] = clothes.get(value, 0) + 1
    
    ret = 1

    # 옷 종류의 (가짓수 + 1)을 서로 곱해줌.
    # +1을 하는 이유는 선택하지 않는 경우를 포함해야되기 때문.
    for val in clothes.values():
        ret *= (val + 1)
    
    print(ret - 1)  # 알몸인 경우를 제외해야하기 때문에 -1 후 리턴
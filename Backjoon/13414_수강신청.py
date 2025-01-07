# 문제집 - 0x15강 - 해시


# 문제: https://www.acmicpc.net/problem/13414
# 메모리: 63588KB / 시간: 332ms
from sys import stdin


input = stdin.readline

K, L = map(int, input().split())
lst = {input().rstrip(): i for i in range(L)}  # int(input())으로 처리할경우 0으로 시작하는 학번을 제대로 처리하지 못함.

passed = sorted(lst, key=lambda x: lst[x])
print(*passed[:K], sep="\n")
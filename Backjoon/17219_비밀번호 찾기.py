# 문제집 - 0x15강 - 해시


# 문제: https://www.acmicpc.net/problem/17219
# 메모리: 48452KB / 시간: 204ms
from sys import stdin


input = stdin.readline

N, M = map(int, input().split())
password = {}

for _ in range(N):
    site, pwd = input().rstrip().split()
    password[site] = pwd

for _ in range(M):
    site = input().rstrip()
    print(password[site])
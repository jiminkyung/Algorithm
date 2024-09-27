# 문자열


# 문제: https://www.acmicpc.net/problem/10809
# 메모리: 31120KB / 시간: 40ms
from sys import stdin


input = stdin.readline
# 유니코드 상 a = 97

alphabet = [-1] * 26

for i, alp in enumerate(input().rstrip()):
    if alphabet[ord(alp) - 97] == -1:
        alphabet[ord(alp) - 97] = i

print(*alphabet)
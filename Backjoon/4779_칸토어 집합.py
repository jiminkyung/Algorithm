# 재귀
# AI의 도움을 받아 푼 문제. 처음에는 리스트를 사용했으나 실패.
# 메모리: 32500KB / 시간: 32ms

from sys import stdin


def cantor(n):
    if n == 0:
        return "-"
    
    prev = cantor(n - 1)
    return prev + " " * (3 ** (n - 1)) + prev

for line in stdin:
    n = int(line.strip())
    print(cantor(n))


# 처음에 구상했던 코드. 방법이 아닌 풀이 과정이 잘못됐던거였다.
# 메모리: 36652KB / 시간: 92ms
from sys import stdin


def cantor(start, end, lines):
    if end - start == 1:
        return
    
    third = (end - start) // 3
    for i in range(start + third, start + 2*third):
        lines[i] = " "
    
    cantor(start, start + third, lines)
    cantor(start + 2*third, end, lines)

for line in stdin:
    n = int(line.strip())
    if n == 0:
        print("-")
    else:
        lines = ["-"] * (3**n)
        cantor(0, 3**n, lines)
        print("".join(lines))
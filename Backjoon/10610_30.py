# 문제집 - 0x12강 - 수학


# 문제: https://www.acmicpc.net/problem/10610

# 1. 뇌 안쓰고 푼 코드
# 메모리: 42920KB / 시간: 168ms
from sys import stdin
from itertools import combinations


input = stdin.readline

N = sorted(input().rstrip(), reverse=True)

if "0" not in N:
    print(-1)
else:
    N = N[:-1]
    ret = 0

    for comb in combinations(N, len(N)):
        num = int("".join(comb))
        if num % 3 == 0:
            ret = max(ret, num)
    if ret > 0:
        print(str(ret) + "0")
    else:
        print(-1)


# 2. 규칙을 이용한 숏코딩!
# ⭐ 3과 9는 자릿수의 합이 3, 9로 나누어 떨어지면 3의 배수, 9의 배수임을 확인할 수 있다.
# 출처: https://www.acmicpc.net/source/85212999
s = input()
print(-1 if not '0' in s or sum(map(int,s)) % 3 != 0 else ''.join(sorted(s,reverse=True)))
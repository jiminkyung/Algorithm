# 문제집 - 0x12강 - 수학


# 문제: https://www.acmicpc.net/problem/1038


# 1. combinations 모듈을 사용한 버전
# 참고 1👉 https://velog.io/@sugyeonghh/%EB%B0%B1%EC%A4%80-1038-%EA%B0%90%EC%86%8C%ED%95%98%EB%8A%94-%EC%88%98Python
# 참고 2👉 https://velog.io/@rhdmstj17/%EB%B0%B1%EC%A4%80-1038%EB%B2%88-%EA%B0%90%EC%86%8C%ED%95%98%EB%8A%94-%EC%88%98-python-%EB%B0%B1%ED%8A%B8%EB%9E%98%ED%82%B9
# 메모리: 32412KB / 시간: 36ms
from itertools import combinations


N = int(input())
ret = []

for i in range(1, 11):
    for j in combinations(range(9, -1, -1), i):
        num = "".join(list(map(str, list(j))))
        ret.append(int(num))

ret.sort()
if N >= len(ret):
    print(-1)
else:
    print(ret[N])


# 2. 백트래킹
# 메모리: 32412KB / 시간: 40ms
N = int(input())
ret = []

def dfs(comb, last, length):
    if len(comb) == length:
        ret.append(int("".join(map(str, comb))))
        return
    
    for i in range(last-1, -1, -1):
        comb.append(i)
        dfs(comb, i, length)
        comb.pop()

for length in range(1, 11):
    dfs([], 10, length)

ret.sort()
print(ret[N] if N < len(ret) else -1)